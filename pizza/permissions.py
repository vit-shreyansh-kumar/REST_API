from rest_framework.permissions import BasePermission
from datetime import datetime

__all__ = [
    'IsBookingOwner',
    'IsOrderAlterable'
]


class IsBookingOwner(BasePermission):
    message = "You must be the owner of this Booking."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.user == request.user):
            return True
        else:
            return False


class IsOrderAlterable(BasePermission):
    message = "Order cannot be cancelled or modified."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.user == request.user):
            time_lapsed = (object.order_date - datetime)

            if time_lapsed > 10:
                return False
            else:
                return True


