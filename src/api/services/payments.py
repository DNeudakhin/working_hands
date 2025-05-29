from typing import Any

from django.db import transaction

from api.repositories import OrganizationsRepository, PaymentsRepository
from api.serializers import PaymentsSerializer
from core.logger import get_logger

loger = get_logger(__name__)


class PaymentsService:
    @staticmethod
    def process_payment(data: dict[str, Any]) -> bool:
        loger.info('Validate income data')
        serializer = PaymentsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data: dict = serializer.validated_data

        loger.info('Get or create org payer')
        organization, _ = OrganizationsRepository.get_or_create(
            inn=validated_data.pop('payer_inn')
        )

        with transaction.atomic():
            loger.info('Get for update with lock org payer')
            organization = OrganizationsRepository.get_with_lock(
                model_id=organization.id
            )

            loger.info('Get or create payment')
            payment, created = PaymentsRepository.get_or_create(
                operation_id=validated_data.pop('operation_id'),
                defaults={
                    **validated_data,
                    'organization_id': organization,
                }
            )

            if created:
                organization.balance += payment.amount
                organization.save()
                loger.info('Balance updated')

        return created
