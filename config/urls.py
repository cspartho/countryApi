from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('country_app.urls')),
    path('api/', include('country_app.api.urls')),

    
]
