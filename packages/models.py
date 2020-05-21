from django.db import models


class Package(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
