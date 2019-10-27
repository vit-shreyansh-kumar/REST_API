from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ListPizza.as_view(), name='listpizza'),
    path('add/', AddPizza.as_view(), name='addpizza'),
    path('update/', UpdatePizza.as_view(), name='updatepizza'),
    path('type/add/', AddPizzaType.as_view(), name='addpizzatype'),
    path('topping/add', AddTopping.as_view(), name='addtopping'),
    path('topping/Update', UpdateTopping.as_view(), name='updatetopping'),
    path('order/add/', AddOrder.as_view(), name="addorder"),
    path('order/update/', UpdateOrder.as_view(), name="updateorder"),
    path('drinks/add/', AddDrink.as_view(), name="adddiscount"),
    path('size/add/', AddPizzaSize.as_view(), name='addpizzasize'),
    path('discount/add/', AddDiscount.as_view(), name="adddiscount"),
    path('discount/update/', UpdateDiscount.as_view(), name='updatediscount')
]
