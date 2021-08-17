from rest_framework import serializers
from ..models import Countries

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields=['name','id','slug','population','alphacode2']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }