import os
from datetime import datetime

import requests
from django.shortcuts import render
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")
# Create your views here.


def home(request):
    r = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q=kampala,UG&appid={API_KEY}"
    ).json()[0]

    lat = r.get("lat")
    lon = r.get("lon")
    data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
    ).json()

    time = datetime.now()
    return render(request, "weather/home.html", {"data": data, "time": time})


def about(request):

    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    items = r.json()[:10]

    return render(request, "weather/about.html", {"items": items})
