from rest_framework import generics
from ..models import Countries
from .serializers import CountrySerializer
class CountryListView(generics.ListCreateAPIView):
    queryset= Countries.objects.all()
    serializer_class = CountrySerializer

class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Countries.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'slug'
