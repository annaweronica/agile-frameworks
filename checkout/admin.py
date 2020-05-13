from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('date', 'total')

    fields = ('name', 'group_size', 'full_name',
              'email', 'phone_number', 'country',
              'town_or_city', 'street_address1',
              'street_address2', 'date', 'price', 'total')

    list_display = ('date', 'full_name',
                    'total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
