from django.shortcuts import render
from .models import ActivitiesItem
from django.http import HttpResponseRedirect

def addActivitiesItem(request):
    x = request.POST['content']
    new_item = ActivitiesItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/')

def thingsToDo(request):
    all_activities_items = ActivitiesItem.objects.all()
    return render(request, 'activities.html', {'all_items':all_activities_items})
