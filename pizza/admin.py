from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Country)
admin.site.register(PizzaType)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Order)
admin.site.register(Drink)
admin.site.register(Size)
admin.site.register(Payment)
admin.site.register(Discount)
admin.site.register(UserSource)