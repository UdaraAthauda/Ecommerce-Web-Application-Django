from django.contrib import admin
from .models import *

admin.site.register(Order)
admin.site.register(OrderItem)

# create an order item inline
class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0

# extend order model
class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderItemInline]
    readonly_fields = ["date_ordered"]

admin.site.unregister(Order)

admin.site.register(Order, OrderAdmin)

