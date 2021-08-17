from django.urls import path
from .views import CountryList,country_list
from .services import get_country_info
urlpatterns = [
    path('', CountryList.as_view(), name='country_list'),
    # path('',country_list,name='country_list'),

]
#get_country_info()