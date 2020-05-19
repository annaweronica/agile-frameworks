from django.contrib import admin
from .models import Package

# Register your models here.


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        # 'p_id',
        'name',
        'description',
        'price',
        'rating',
        'image_url',
        # 'image',
    )

    ordering = ('name',)


admin.site.register(Package, PackageAdmin)
