from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('country_app.urls')),
    path('api/', include('country_app.api.urls')),
    
]
