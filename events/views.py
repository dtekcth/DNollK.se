from django.shortcuts import render

from arr.models import Event

def index(request):
    events = Event.objects.all()
    return render(request, "events/index.dtl", { 'events' : events })
