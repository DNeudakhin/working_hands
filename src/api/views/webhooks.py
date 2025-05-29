import datetime
import traceback
from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.views import APIView

from api.services import PaymentsService
from core.logger import get_logger

loger = get_logger(__name__)


class PaymentWebhookView(APIView):
    @staticmethod
    def post(request):
        try:
            loger.info('Start processing payment')
            created = PaymentsService.process_payment(request.data)
            if not created:
                loger.info('Payment with operation_id'
                           f' {request.data["operation_id"]} already'
                           ' processed')
                return Response(status=HTTPStatus.OK)

            loger.info('Balance successfully increased'
                       f' for {request.data["payer_inn"]}'
                       f' on {request.data["amount"]}'
                       f' at {datetime.datetime.now()}')
            return Response(status=HTTPStatus.CREATED)
        except Exception as e:
            loger.exception(traceback.format_exc())
            raise e
