from django.db import models


class Basket(models.Model):
    # b_id = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    group = models.CharField(max_length=254)
    # group_size = models.IntegerField(default=1)
    # date = models.DateField(auto_now=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

# class BasketLineItem(models.Model):
#     """attaches to an order and a package"""
#     basket = models.ForeignKey(Basket, null=False, blank=False, on_delete=models.CASCADE)
#     package = models.ForeignKey(Package, null=False, blank=False, on_delete=models.CASCADE)
#     lineitem_total = models.DecimalField(max_digits=6, decimal_places=2)
