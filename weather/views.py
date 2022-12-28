import os
from datetime import datetime

import requests
from django.shortcuts import render
from dotenv import load_dotenv

# loading environment variables
load_dotenv()

API_KEY = os.environ.get("API_KEY")


# Create your views here.


def home(request):
    # checking if city has been searched, otherwise render Use Kampala as the default city

    if request.method == "POST":
        error = ""
        data = ""
        city = request.POST.get("search")

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
        else:
            error = "City Does Not Exist, Ensure it is spelt correctly"

        # Get current system time
        time = datetime.now()

        return render(
            request, "weather/home.html", {"data": data, "time": time, "error": error}
        )

    else:
        city = "kampala"
        r = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}"
        ).json()

        lat = r[0].get("lat")
        lon = r[0].get("lon")
        data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
        ).json()

        # Get current system time
        time = datetime.now()
        return render(request, "weather/home.html", {"data": data, "time": time})
