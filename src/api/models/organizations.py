from decimal import Decimal

from django.db import models


class Organizations(models.Model):
    inn = models.CharField(max_length=12, unique=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2,
                                  default=Decimal(0.00))
