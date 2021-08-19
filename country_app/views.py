from django.shortcuts import render
from .models import Countries,NeighbourCountry
from django.shortcuts import get_object_or_404

import requests

from django.views.generic import TemplateView,ListView,DetailView
from .services import get_country_info

class CountryList(ListView):
    model = Countries
    template_name = 'country/home.html'

    def get_context_data(self, **kwargs):   
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('name',None)
        if query:
            context['query'] = Countries.objects.filter(name__icontains=query).order_by('name')
        
        countries=Countries.objects.all().order_by('name')
        context['countries']=countries
        return context
    
class CountryDetail(DetailView):
    model=Countries
    template_name= 'country/country_detail.html'
    context_object_name = 'countries'
    queryset = Countries.objects.all()

    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['neighbour'] = get_object_or_404(NeighbourCountry, id=self.object.id)
    #     return context
