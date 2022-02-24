from django.urls import path
from .views import index, home

app_name= "doctors"

urlpatterns = [
    path('', index, name="index"),
    path('home', home, name="home"),
]
