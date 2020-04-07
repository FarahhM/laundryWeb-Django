from django.contrib import admin
from .models import Classification, Item, OrderItem, UserOrder, Service


admin.site.register(Classification)
admin.site.register(Service)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(UserOrder)
