"""bookings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from flights import views
from pizza.api.viewsets import *
from pizza.views import *

router = routers.DefaultRouter()

"""
API Routing
"""
router.register(r'country',CountryViewSet,base_name='country')


            # 'AddOrder',
            # 'UpdateOrder',
            # 'AddDrink',
            # 'AddPizzaSize',
            # 'AddDiscount',
            # 'UpdateDiscount'

urlpatterns = [
    # url(r'^', include('login.urls', namespace="login")),
    path('admin/', admin.site.urls),
    path('pizza/', include('pizza.urls')),
    path('flights/', views.FlightsList.as_view(), name="flights-list"),
    
    path('bookings/', views.BookingsList.as_view(), name="bookings-list"), 
    path('booking/<int:booking_id>/', views.BookingDetails.as_view(), name="booking-details"),
    path('booking/<int:booking_id>/update/', views.UpdateBooking.as_view(), name="update-booking"),
    path('booking/<int:booking_id>/cancel/', views.CancelBooking.as_view(), name="cancel-booking"),
    path('book/<int:flight_id>/', views.BookFlight.as_view(), name="book-flight"),

    path('profile/', views.ProfileDetails.as_view(), name="profile-details"),
    path('login/', TokenObtainPairView.as_view(), name="login"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token-refresh"),
    path('register/', views.Register.as_view(), name="register"),
    path('addgroup/', views.CreateGroup.as_view(), name='addgroup'),

    path('pizza/',ListPizza.as_view(), name='pizza-detail'),
    path('pizza/<int:pizza_id>', PizzaDetails.as_view(), name='pizza-detail'),
    path('pizza/add/',AddPizza.as_view(), name='addpizza'),
    path('pizza/delete/<int:pizza_id>',DeletePizza.as_view(), name='deletepizza'),
    path('pizza/update/<int:pizza_id>',UpdatePizza.as_view(), name='udatepizza'),

    path('topping/',ListTopping.as_view(), name='topping'),
    path('topping/add/',AddTopping.as_view(), name='addtopping'),
    path('topping/update/<int:topping_id>',UpdateTopping.as_view(), name='updatetopping'),
    path('topping/delete/<int:topping_id>',DeleteTopping.as_view(), name='deletetopping'),

    path('size/', ListPizza.as_view(), name='size-detail'),

    url(r'^api/', include(router.urls))
]
