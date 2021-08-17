from rest_framework import generics,filters
from ..models import Countries
from .serializers import CountrySerializer
from django_filters.rest_framework import DjangoFilterBackend

class CountryListView(generics.ListCreateAPIView):
    search_fields = ['name']
    serializer_class = CountrySerializer
    queryset= Countries.objects.all()
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    filterset_fields = ['name','slug','neighbouring_countries','languages']

class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Countries.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'slug'


