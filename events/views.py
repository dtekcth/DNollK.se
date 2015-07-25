from django.shortcuts import render

from events.models import Event

def index(request):
    events = Event.get_grouped_by_date()
    return render(request, "events/index.dtl", { 'events' : events })
