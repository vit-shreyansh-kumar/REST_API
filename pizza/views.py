from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView,DetailView,DeleteView,CreateView
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,\
    DestroyAPIView,ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView,RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from .api.serializers import *
from .models import *
from .permissions import *

# Create your views here.

__all__ = [
            'ListPizza',
            'AddPizza',
            'UpdatePizza',
            'PizzaDetails',
            'AddPizzaType',
            'DeletePizza',
            'ListTopping',
            'AddTopping',
            'UpdateTopping',
            'DeleteTopping',
            'AddOrder',
            'UpdateOrder',
            'AddDrink',
            'AddPizzaSize',
            'AddDiscount',
            'UpdateDiscount'
]


class ListPizza(ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    # permission_classes = [IsAuthenticated]

class PizzaDetails(RetrieveAPIView):
    queryset = Pizza.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'pizza_id'
    serializer_class = PizzaDetailsSerializer

class AddPizza(CreateAPIView):

    serializer_class = PizzaSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    # permission_classes = [IsAuthenticated]


class UpdatePizza(UpdateAPIView):
    serializer_class = AdminUpdatePizzaSerializer
    permission_classes = [IsAuthenticated]


class DeletePizza(DestroyAPIView):
    serializer_class = AdminUpdatePizzaSerializer
    permission_classes = [IsAuthenticated]


class AddPizzaType(CreateAPIView):
    serializer_class = PizzaTypeSerializer
    # permission_classes = [IsAuthenticated]


class ListTopping(ListAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingsSerializer
    # permission_class


class AddTopping(CreateAPIView):
    serializer_class = ToppingsSerializer
    # permission_classes = [IsAuthenticated]


class UpdateTopping(RetrieveUpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Topping.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'topping_id'
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return AdminUpdateToppingsSerializer
        else:
            return UpdateToppingSerializer


class DeleteTopping(DestroyAPIView):
    queryset = Topping.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'topping_id'
    # permission_classes = [IsAuthenticated]


class ListSize(ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class ListOrder(ListAPIView):

    queryset = Order.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticated]


class AddOrder(CreateAPIView):
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticated]


class UpdateOrder(UpdateAPIView):
    serializer_class = AdminUpdateOrderSerializer
    permission_classes = [IsAuthenticated, IsBookingOwner, IsOrderAlterable]


class AddDrink(CreateAPIView):
    serializer_class = DrinksSerializer
    permission_classes = [IsAuthenticated]


class AddPizzaSize(CreateAPIView):
    serializer_class = SizeSerializer
    # permission_classes = [IsAuthenticated]


class AddDiscount(CreateAPIView):
    serializer_class = DiscountSerializer
    permission_classes = [IsAuthenticated]


class UpdateDiscount(UpdateAPIView):
    serializer_class = AdminUpdateDiscountSerializer
    permission_classes = [IsAuthenticated]