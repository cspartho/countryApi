from django.urls import path
from .views import CountryListView,CountryDetailView

urlpatterns = [
    path('country/list/',CountryListView.as_view(),name='country_list'),
    path('country/<slug:slug>',CountryDetailView.as_view(),name='country_detail')
]