from django.db import models
from django.utils import timezone


class Sale(models.Model):
    transaction_id = models.CharField(max_length=50, unique=True)
    transaction_date = models.DateField()
    transaction_time = models.TimeField()
    transaction_qty = models.IntegerField()
    store_id = models.IntegerField()
    store_location = models.CharField(max_length=100)
    product_id = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_category = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_detail = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, Date: {self.transaction_date}, Time: {self.transaction_time}"
