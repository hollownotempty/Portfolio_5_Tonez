import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from store.models import Packs

# Create your models here.

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=58, null=False, blank=False)
    email = models.EmailField(max_length= 254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """ Generate random order number"""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Update grand total """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        """ Override default save method """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Packs, null=False, blank=False, on_delete=models.CASCADE)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """ Override default save method """
        self.lineitem_total = self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product} on order {self.order.order_number}'
