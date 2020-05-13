from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=254)
    group_size = models.IntegerField(default=1)
    date = models.DateField(auto_now=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class OrderLineItem(models.Model):
     """attaches to an order and a package"""

     order = models.ForeignKey(Basket, null=False, blank=False, on_delete=models.CASCADE)
     package = models.ForeignKey(Package, null=False, blank=False, on_delete=models.CASCADE)
     lineitem_total = models.DecimalField(max_digits=6, decimal_places=2)
