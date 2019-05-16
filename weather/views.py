from django.shortcuts import render
import django.contrib.sites.requests
import requests
# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8db91afbbebc6c6b2fb7ac46b1803961'
    city= 'Las Vegas'
    r=requests.get(url.format(city)).json()

    city_weather={
        'city':city,
        'temperature':r['main']['temp'],
        'desription':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon'],
    }

    return render(request, 'weather/weather.html')

    print(city_weather)