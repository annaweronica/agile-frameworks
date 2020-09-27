from django.contrib import admin
from .models import Package


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)


admin.site.register(Package, PackageAdmin)
