import os
import requests
from .models import Countries

def get_country_info():
    all_countries ={}
    url = 'https://restcountries.eu/rest/v2/all'
    response = requests.get(url)
    data = response.json()

    country_list=[]

    for i in data:
        country_data = Countries(
        name = i['name'],
        alphacode2 = i['alpha2Code'],
        capital = i['capital'],
        population = i['population'],
        timezone = ' '.join(map(str,i['timezones'])),
        flag_url = i['flag'],
        languages = str(i['languages']),
        neighbouring_countries =str(i['borders'])
        )
        country_data.save()
        country_list.append(i)
    

    return country_list
        


