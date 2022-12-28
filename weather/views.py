import os
from datetime import datetime

import requests
from django.shortcuts import render
from dotenv import load_dotenv

# loading environment variables
load_dotenv()

API_KEY = os.environ.get("API_KEY")

# Get current system time
time = datetime.now()


def get_data(city):
    r = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}"
    ).json()

    if len(r) != 0:

        # Get latitude and longitude of city
        lat = r[0].get("lat")
        lon = r[0].get("lon")
        data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
        ).json()
        return data
    else:
        return False


# Create your views here.


def home(request):
    # checking if city has been searched, otherwise render Use Kampala as the default city

    if request.method == "POST":
        city = request.POST.get("search")

        data = get_data(city)

        return render(request, "weather/home.html", {"data": data, "time": time})

    else:
        data = get_data("kampala")

        return render(request, "weather/home.html", {"data": data, "time": time})
