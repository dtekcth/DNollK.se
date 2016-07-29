from django.shortcuts import render

from events.models import Event

"""
Event view module.

In this module we list the views that contains the logic to the templates
and also provides them with the data they show.
"""

def index(request):
    """
    Gets all events for the current year and renders them on a page.
    """
    events = Event.get_grouped_by_date()
    return render(request, "events/index.dtl", { 'events' : events })

def index_from_year(request, year):
    """
    Gets all events for a requested year and renders them on a page.
    """
    events = Event.get_grouped_by_date_and_year(year)
    return render(request, "events/index.dtl", { 'events' : events})
