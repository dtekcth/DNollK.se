from django.db import models
from datetime import datetime

import itertools

class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateTimeField('datum')
    text = models.TextField()

    def __str__(self):
        return self.name

    @staticmethod
    def get_grouped_by_date_and_year(year):
        """
        Retrieves all events grouped by date from the given year.

        Iterates all events and checks if the date of that event exists in
        grouped_events.
        If that is the case it appends the event to that list, otherwise it
        creates a singleton list with that event.
        """
        if year == None:
            events = Event.objects.order_by('date')
        elif len(year) != 4:
            raise ValueError("year must be of form YYYY")
        else:
            events = Event.objects.filter(date__year=year)

        return Event.group_by_date(events)

    @staticmethod
    def get_grouped_by_date():
        """
        Retrieves all events grouped by date from the current year.

        Iterates all events and checks if the date of that event exists in
        grouped_events.
        If that is the case it appends the event to that list, otherwise it
        creates a singleton list with that event.
        """
        year = str(datetime.now().year)
        return Event.get_grouped_by_date_and_year(year)

    @staticmethod
    def get_all_grouped_by_date():
        """
        Retrieves all events grouped by date.

        Iterates all events and checks if the date of that event exists in
        grouped_events.
        If that is the case it appends the event to that list, otherwise it
        creates a singleton list with that event.
        """
        return Event.get_grouped_by_date_and_year(None)

    @staticmethod
    def group_by_date(es):
        """
        Groups a list of event by date.
        The returned structure is a list of list of events where every list of
        events contains events from one date.
        """
        eList = []

        for d, es_by_date in itertools.groupby(es, lambda e: e.date.date()):
            eList.append(list(es_by_date))

        return eList
