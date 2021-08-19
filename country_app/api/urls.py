from django.urls import path
from .views import CountryListView,CountryDetailView,BorderListView

urlpatterns = [
    path('country/list/',CountryListView.as_view(),name='country_list'),
    path('country/<slug:slug>/',CountryDetailView.as_view(),name='country_detail'),
    path('country/',BorderListView.as_view(),name='border_list'),
]