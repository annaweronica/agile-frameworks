from django.contrib import admin
from .models import Package

# Register your models here.


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Package, PackageAdmin)
