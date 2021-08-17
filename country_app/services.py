import os
import requests
from .models import Countries

def get_country_info():
    all_countries ={}
    url = 'https://restcountries.eu/rest/v2/all'
    response = requests.get(url)
    data = response.json()

    country_list=[]
    d={}
    for j in data:
        key=j['alpha3Code']
        value=j['name']
        d[key]=value

    for i in data:
        l=[]
        for j in i['languages']:
           l.append(j['name']) 
        
        nc=i['borders']
        blist=[]
        for m in nc:
            blist.append(d[m])

        country_data = Countries(
        name = i['name'],
        alphacode2 = i['alpha2Code'],
        capital = i['capital'],
        population = i['population'],
        timezone = ' '.join(map(str,i['timezones'])),
        flag_url = i['flag'],
        languages = ','.join(l),
        neighbouring_countries =','.join(blist)
        )
        country_data.save()
        country_list.append(i)
    

    return country_list
        


