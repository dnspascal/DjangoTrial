from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def homepageview(request):
    return HttpResponse("Hello, world now")

class HomePageView(TemplateView):
    template_name = "home.html"
class AboutPageView(TemplateView):
    template_name = "about.html "
# Create your views here.
