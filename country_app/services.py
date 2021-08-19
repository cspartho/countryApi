import os
import requests
from .models import Countries, NeighbourCountry

def get_country_info():
    all_countries = {}
    url = 'https://restcountries.eu/rest/v2/all'
    response = requests.get(url)
    data = response.json()

    country_list = []
    d = {}
    for j in data:
        key = j['alpha3Code']
        value = j['name']
        d[key] = value
    s=0
    for i in data:
        l = []
        s+=1
        nc = i['borders']
        if nc:
            for m in nc:
                api_neighbour_name=str(d[m])
        else:
            api_neighbour_name="NULL"
        
        for j in i['languages']:
            l.append(j['name'])

        if l:
            api_neighbour_languages = ','.join(l)
        else:
            api_neighbour_languages = "NULL"
       
        country_data = Countries(
            name=i['name'],
            alphacode2=i['alpha2Code'],
            capital=i['capital'],
            population=i['population'],
            timezone=' '.join(map(str, i['timezones'])),
            flag_url=i['flag'],
        )
        country_data.save()
        NeighbourCountry.objects.create(nname=api_neighbour_name,
            nlanguages=api_neighbour_languages,ncountry_id =s
            )
       

        l.clear()
        country_list.append(i)
    

    # for im in data:
    #     nc = im['borders']
    #     border = Countries.objects.get(id=pk)
    #     if nc:
    #         for m in nc:
    #             neighbour_data = NeighbourCountry(border_country_name=str(d[m]))
    #     else:
    #         neighbour_data= NeighbourCountry(border_country_name="NULL")
    #     neighbour_data.save()
    
    # for il in data:
    #     l = []
       
    #     for j in il['languages']:
    #         l.append(j['name'])
    #     if l:
    #         border_language_data = Languages(
    #             border_languages_list = ','.join(l)
   
    #         )
    #         l.clear()
    #     else:
    #         border_language_data = Languages(
    #             border_languages_list = "NULL"
    #         )
        
    #     border_language_data.save()
    
    return country_list
