import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from packages.models import Package

class Order(models.Model):
    name = models.CharField(max_length=254)
    group_size = models.IntegerField(default=1)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateField(auto_now=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update total each time a line item is added.
        """
        self.total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        self.save()


class OrderLineItem(models.Model):
     """attaches to an order and a package"""
     # it is like an individual shopping bag item relating to a specific order

     order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE)
     package = models.ForeignKey(Package, null=False, blank=False, on_delete=models.CASCADE)
     lineitem_total = models.DecimalField(max_digits=6, decimal_places=2)
