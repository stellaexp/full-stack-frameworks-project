from django.contrib import admin
from .models import CustomerOrder, OrderItem


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('line_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdmin,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'telephone', 'address1',
              'address2', 'address3', 'postcode',
              'county', 'country', 'delivery_cost',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(CustomerOrder, OrderAdmin)
