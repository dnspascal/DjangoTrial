from django.urls import path
from .views import homepageview, HomePageView, AboutPageView

urlpatterns = [
    path('hello/', homepageview, name='hello'),
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]
