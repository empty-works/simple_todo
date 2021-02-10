from django.shortcuts import render
from .models import ActivitiesItem

def thingsToDo(request):
    all_activities_items = ActivitiesItem.objects.all()
    return render(request, 'activities.html', {'all_items':all_activities_items})
