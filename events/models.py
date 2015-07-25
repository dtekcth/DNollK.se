from django.db import models

import itertools

class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateTimeField('datum')
    text = models.TextField()

    def __str__(self):
        return self.name

    def get_grouped_by_date():
        """
        Retrieves all events grouped by date.

        Iterates all events and checks if the date of that event exists in grouped_events.
        If that is the case it appends the event to that list, otherwise it creates a singleton
        list with that event.
        """
        grouped_events = []
        all_events = Event.objects.order_by('date')

        for date, event_list in itertools.groupby(all_events, lambda e: e.date.date()):
            grouped_events.append(list(event_list))
        return grouped_events
