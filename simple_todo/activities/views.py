from django.shortcuts import render

def thingsToDo(request):
    return render(request, 'activities.html')
