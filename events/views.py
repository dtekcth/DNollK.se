# Our own model
from events.models import Event

# Our paginated index function
from dnollkse.views import paginated_index

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
    return paginated_events_index(request, events)


def index_from_year(request, year):
    """
    Gets all events for a requested year and renders them on a page.
    """
    events = Event.get_grouped_by_date_and_year(year)
    return paginated_events_index(request, events)


def paginated_events_index(request, events):
    """
    Wraps the generic dnollkse.views.paginated_index to a events-specific
    function.
    """
    return paginated_index(request, events, 'events/index.dtl', 'items')
