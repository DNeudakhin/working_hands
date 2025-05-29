from rest_framework import serializers

from api.models import Organizations


class OrganizationsBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields = ('inn', 'balance')
