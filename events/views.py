from django.shortcuts import render

from events.models import Event

def index(request):
    events = Event.objects.all()
    return render(request, "events/index.dtl", { 'events' : events })
