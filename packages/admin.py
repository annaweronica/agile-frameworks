from django.contrib import admin
from .models import Package

# Register your models here.


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        # 'p_id',
        'name',
        'price',
        'rating',
        'image',
    )

    # ordering = ('p_id',)


admin.site.register(Package, PackageAdmin)
