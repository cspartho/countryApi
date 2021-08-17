from rest_framework import serializers
from ..models import Countries

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields=['name','alphacode2','slug','capital','population','timezone','languages','neighbouring_countries']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class BorderCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields =['name']