from django.urls import path
from .views import CountryList,CountryDetail
from .services import get_country_info

app_name = 'country_app'
urlpatterns = [
    path('', CountryList.as_view(), name='country_list'),
    path('country/<slug:slug>/',CountryDetail.as_view(),name='country_detail'),
]
get_country_info()
