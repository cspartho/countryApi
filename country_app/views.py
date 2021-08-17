from django.shortcuts import render
from .models import Countries

import requests

from django.views.generic import TemplateView,ListView
from .services import get_country_info
from django.core.paginator import Paginator
from django.apps import AppConfig


# class CountryList(TemplateView):
#     template_name = 'country/home.html'
    
#     def get_context_data(self, *args, **kwargs):
#         context = {
#             'countries': get_country_info(),
#         }
#         return context
class CountryList(ListView):
    model = Countries
    template_name = 'country/home.html'
    context_object_name = 'countries'
    queryset = Countries.objects.all()
    paginate_by = 15


# def country_list(request):
#     paginator = Paginator(get_country_info(), 4)

#     page_number =request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#             'countries': get_country_info(),
#             'page_obj': page_obj,
#         }
#     return render(request, 'country/home.html', context)