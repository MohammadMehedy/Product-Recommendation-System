from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(CartItem)
admin.site.register(PurchaseInfo)
admin.site.register(OrderedProduct)
admin.site.register(UserRating)