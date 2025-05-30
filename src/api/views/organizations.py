from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.views import APIView

from api.services import OrganizationsService


class OrganizationBalanceView(APIView):
    @staticmethod
    def get(request, inn: str) -> Response:
        balance = OrganizationsService.show_balance(inn)
        return Response(
            status=HTTPStatus.OK,
            data=balance,
        )
