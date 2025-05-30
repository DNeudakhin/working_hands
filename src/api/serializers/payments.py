import re
import uuid
from decimal import Decimal

from rest_framework import serializers


class PaymentsSerializer(serializers.Serializer):
    operation_id = serializers.UUIDField(default=uuid.uuid4)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2,
                                      min_value=Decimal(0.01))
    payer_inn = serializers.CharField(min_length=10, max_length=12)
    document_number = serializers.CharField(max_length=50)
    document_date = serializers.DateTimeField()

    @staticmethod
    def validate_payer_inn(value) -> str:
        if not re.match(r'^\d{10}$|^\d{12}$', value):
            raise serializers.ValidationError("INN must be 10 or 12 digits.")
        return value
