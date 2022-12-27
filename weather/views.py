from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Home(TemplateView):
    template_name = "weather/home.html"


class About(TemplateView):
    template_name = "weather/about.html"


# def Home(request):
#     return HttpResponse("Home")


# def About(request):
#     return HttpResponse("About")
