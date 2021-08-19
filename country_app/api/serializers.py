from rest_framework import serializers
from ..models import Countries,NeighbourCountry

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields=['name','alphacode2','slug','capital','population','timezone']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class BorderCountrySerializer(serializers.ModelSerializer):
    borders = CountrySerializer(many=True)
    class Meta:
        model = NeighbourCountry
        fields =['border','nname']