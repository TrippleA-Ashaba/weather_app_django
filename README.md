![image](https://user-images.githubusercontent.com/102288573/209771205-6878b839-6798-4736-a093-8fd054c62b40.png)
# weather_app_django


A mobile responsive, with city search functionaliy, weather app using the [Open Weather api](https://openweathermap.org/).

## How Install

After forking the repository, create a virtual environment on the same level as the *django_project*

```
$ python -m venv .venv
```

Then activate the environment

```
$ source .venv/Scripts/activate
```

Then install all dependencies from the requirements.txt file

```
$ pip install -r requirements.txt
```
Still on the django_project level, create a *.env* file, Here we shall put our API_KEY and SECRET_KEY
```
SECRET_KEY = "this is my secret key"
API_KEY = "api_key_from_openweathermap"
```

## Start Using App

You can straight away start using the weather app
```
$ python manage.py runserver
```
Or copy the weather app contents and use in another project.
Then register the app in *django_project/settings.py* installed apps

```diff
INSTALLED_APPS = {
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
   
    "weather.apps.WeatherConfig", #new
    
}
```


### ENJOY
