from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

__all__ = [
    'Country',
    'PizzaType',
    'Pizza',
    'Topping',
    'Order',
    'Drink',
    'Size',
    'Discount',
    'Payment',
    'UserSource',
]


"""
# Define your custom validators here.
"""


def code_validator(code):
    code = str(code)
    print(code)
    length = len(code)

    if length >5:
        raise ValidationError(
            '(%code) is invalid, should be less than 5 chars',
            params={'value': code}
        )


def numbervalidator(phone):
    phone = str(phone)
    length = len(phone)
    if length < 10:
        raise ValidationError(
            '(%phone)s is invalid',
            params={'value': phone}
        )
    elif length > 10:
        raise ValidationError(
            '(%phone)s is invalid',
            params={'value': phone}
        )


class Payment(models.Model):
    PAYMENT_METHOD = (('ONL', 'Online'),
                      ('VISA', 'Visa'),
                      ('RUPAY', 'RuPay'),
                      ('PAYTM', 'PayTM'),
                      ('MASTR', 'Master Card'),
                      ('DBTC', 'Debit Card'),
                      ('CRDT', 'Credit Card'),
                      ('COD', 'Cash On Delivery'),
                      ('RAZP', 'RazorPay'))

    name = models.CharField(max_length=20, blank=False, validators=[code_validator])
    method = models.CharField(
        max_length=5,
        choices=PAYMENT_METHOD
    )
    status = models.BooleanField(default=True)


class UserSource(models.Model):
    name = models.CharField(max_length=20, unique=True, blank=False)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=40, unique=True, blank=False)
    code = models.CharField(max_length=5, unique=True, blank=False, validators=[code_validator])

    def __str__(self):
        return self.name


class PizzaType(models.Model):
    type = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return self.type


class Topping(models.Model):
    name = models.CharField(max_length=20, blank=False)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return self.size


class Drink(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=20, blank=False)
    code = models.CharField(max_length=8, blank=False)
    maximum = models.FloatField(default=0.0)
    percent = models.FloatField(default=0.0)
    user_type = models.ForeignKey(
        UserSource,
        on_delete=models.CASCADE,
        verbose_name='source'
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=30, blank=False)
    type = models.ForeignKey(
        PizzaType,
        on_delete=models.CASCADE,
        verbose_name='pizza type'
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
        verbose_name='size'
    )
    toppings = models.ManyToManyField(Topping)
    available = models.BooleanField(default=True)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return "%s: %s" % (self.name, self.type)


class Order(models.Model):
    order_number = models.PositiveIntegerField()
    order_date = models.DateTimeField(default=datetime.now())
    mobile_no = models.BigIntegerField(validators=[numbervalidator])
    email = models.EmailField()
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='customer'
    )
    pizza = models.ForeignKey(
        Pizza,
        on_delete=models.CASCADE,
        verbose_name='pizza'
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        verbose_name='country'
    )
    discount = models.ForeignKey(
        Discount,
        on_delete=models.CASCADE,
        verbose_name='discount'
    )
    payment_method = models.ForeignKey(
        Payment,
        on_delete=models.CASCADE,
        verbose_name='payment'
    )
    total_price = models.FloatField(default=0.0)

    def __str__(self):
        return "%s: %s" % (self.user.username, str(self.order_number))




# class DeliveryBoy(models.Model):
#     pass
#
#
# class Delivery(models.Model):
#     pass