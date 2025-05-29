from django.urls import path

from api.views import PaymentWebhookView
from api.views.organizations import OrganizationBalanceView

urlpatterns = [
    path('webhook/bank/',
         PaymentWebhookView.as_view(),
         name='webhook_bank'),
    path('organization/<inn>/balance',
         OrganizationBalanceView.as_view(),
         name='organization_balance'),
]
