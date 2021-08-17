from django.contrib import admin
from .models import Countries



class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('alphacode2',)}

admin.site.register(Countries,CountryAdmin)