from rest_framework import serializers
from ..models import *

__all__ = [
    'CountrySerializer',
    'PizzaDetailsSerializer',
    'PizzaSerializer',
    'AdminUpdatePizzaSerializer',
    'PizzaTypeSerializer',
    'ToppingsSerializer',
    'AdminUpdateToppingsSerializer',
    'OrdersSerializer',
    'UpdateToppingSerializer',
    'AdminUpdateOrderSerializer',
    'DrinksSerializer',
    'SizeSerializer',
    'DiscountSerializer',
    'AdminUpdateDiscountSerializer'
]


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

    def create(self, validated_data):
        new_country = Country(name=validated_data['name'], code=validated_data['code'])
        new_country.save()
        return validated_data


class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="pizza:pizza-detail")
    class Meta:
        model = Pizza
        fields = ('url','name','type','size','toppings','available')


class AdminUpdatePizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ['available','price']


class PizzaDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza
        fields = ['name', 'type', 'size', 'toppings', 'available', 'price', 'url']


class PizzaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaType
        fields = '__all__'


class ToppingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = '__all__'


class UpdateToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ['name']


class AdminUpdateToppingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ['name','price']


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class AdminUpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['mobile_no', 'payment_method']


class DrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'


class SizeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="pizza:size-detail")
    class Meta:
        model = Size
        fields = ('url','size')


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class AdminUpdateDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['end_date', 'maximum', 'percent', 'user_type', 'status']