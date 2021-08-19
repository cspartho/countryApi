from rest_framework import generics,filters
from ..models import Countries,NeighbourCountry
from .serializers import CountrySerializer,BorderCountrySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import BasePermission, IsAuthenticated

class CountryListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CountrySerializer
    queryset= Countries.objects.all()
    

class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset= Countries.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'slug'

class BorderListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    search_fields = ['name']
    serializer_class = CountrySerializer
    queryset= Countries.objects.all()
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    filterset_fields = ['name','capital','population']

