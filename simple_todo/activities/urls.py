from django.contrib import admin
from django.urls import path
from activities.views import thingsToDo

urlpatterns = [
        path('thingstodo/', thingsToDo)
        ]
