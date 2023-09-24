from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    return render(request,"template_app/first.html")

def weather_view(request):
    weather_dict = {"Ankara" : "28", "Antalya" : "35"}
    return render(request,"template_app/weather.html",context=weather_dict)




