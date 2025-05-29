from api.repositories import OrganizationsRepository
from api.serializers import OrganizationsBalanceSerializer


class OrganizationsService:
    @staticmethod
    def show_balance(inn: str) -> dict:
        org = OrganizationsRepository.get_by_inn(inn=inn)
        return OrganizationsBalanceSerializer(org).data


