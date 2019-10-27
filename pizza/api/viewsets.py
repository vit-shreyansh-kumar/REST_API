from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from ..models import *
from ..permissions import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,RetrieveUpdateAPIView,UpdateAPIView,RetrieveAPIView


__all__ = ['CountryViewSet']

# Create your own view classes here.


class ListCountryViewSet(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name']
    permission_classes = [IsAuthenticated]


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    # permission_classes = [IsAuthenticated]
    queryset = Country.objects.all()
    """
        Create a model instance.
    """

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



