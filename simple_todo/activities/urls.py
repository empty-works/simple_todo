from django.contrib import admin
from django.urls import path
from . import views

app_name = "activities"

urlpatterns = [
        path('', views.thingsToDo, name='activities')
        ]
