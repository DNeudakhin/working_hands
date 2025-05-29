from django.db import models


class Payments(models.Model):
    operation_id = models.CharField(max_length=36, unique=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    organization_id = models.ForeignKey('Organizations',
                                        on_delete=models.CASCADE)
    document_number = models.CharField(max_length=50)
    document_date = models.DateTimeField()
