from django.shortcuts import render
import django.contrib.sites.requests
import pip._vendor.requests.api

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8db91afbbebc6c6b2fb7ac46b1803961'
    city= 'Nairobi'
    
    print(r.text)

    return render(request, 'weather/weather.html')