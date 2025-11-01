from django.urls import path

from .apps import MenuConfig
from .views import home

app_name = MenuConfig.name

urlpatterns = [
    path("", home, name="home"),
]
