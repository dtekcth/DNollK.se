#!/usr/bin/env python

from django.db import models
import json

def is_none_or_empty(str):
    """
    Checks if a string is None or empty string.
    """
    return not str


class Config(models.Model):
    # Social widgets
    instagram_widget_url = models.TextField()
    twitter_widget_id = models.TextField()

    # Calendar
    gcal_api_key = models.TextField(null=True, blank=True)
    gcal_dnollk_calendar_id = models.TextField(null=True, blank=True)
    gcal_dnollk_calendar_url = models.TextField(null=True, blank=True)
    gcal_timeedit_calendar_id = models.TextField(null=True, blank=True)
    gcal_asp_calendar_id = models.TextField(null=True, blank=True)

    # Form
    gform_link = models.TextField(null=True, blank=True)
    gform_embed_link = models.TextField(null=True, blank=True)

    enable_form = models.BooleanField()

    # Logos and headers
    logo_url = models.TextField(default="/static/dnollkse/images/logo.png")
    header_url = models.TextField(default="/static/dnollkse/images/header.jpg")
    favicon_url = models.TextField(null=True, blank=True)

    year = models.CharField(max_length=4, default="2017")

    def is_dnollk_calendar_enabled(self):
        """
        Returns whether the dnollk calendar is enabled
        """
        return not is_none_or_empty(self.gcal_api_key) \
            and not is_none_or_empty(self.gcal_dnollk_calendar_id) \
            and not is_none_or_empty(self.gcal_dnollk_calendar_url)

    def is_timeedit_calendar_enabled(self):
        """
        Returns whether the timeedit (school) calendar is enabled
        """
        return not is_none_or_empty(self.gcal_api_key) \
            and not is_none_or_empty(self.gcal_timeedit_calendar_id)

    def is_asp_calendar_enabled(self):
        """
        Returns whether the asp calendar is enabled
        """
        return not is_none_or_empty(self.gcal_api_key) \
            and not is_none_or_empty(self.gcal_asp_calendar_id)

    def calEventSources(self):
        """
        Returns a python object with the event sources used in FullCalender.
        """
        eventSources = []
        if self.is_dnollk_calendar_enabled:
            eventSources.append({
                'googleCalendarId': self.gcal_dnollk_calendar_id,
                'className': 'eventCalendar',
                'color': "#FA6607"
            })

        if self.is_timeedit_calendar_enabled:
            eventSources.append({
                'googleCalendarId': self.gcal_timeedit_calendar_id,
                'className': 'schoolCalendar',
                'color': 'CornFlowerBlue'
            })

        if self.is_asp_calendar_enabled:
            eventSources.append({
                'googleCalendarId': self.gcal_asp_calendar_id,
                'className': 'aspCalendar'
            })

        return eventSources

    def smallCalendarConf(self):
        return json.dumps({
            'googleCalendarApiKey': self.gcal_api_key,
            'header': {
                'left': 'prev, next',
                'center': 'title',
                'right': 'today'
            },

            'eventSources': self.calEventSources(),
            'weekends': 'true',
            'defaultView': 'agendaDay',
            'height': 500
        })

    def bigCalendarConf(self):
        return json.dumps({
            'googleCalendarApiKey': self.gcal_api_key,
            'header': {
                'left': 'prev,next today',
                'center': 'title',
                'right': 'agendaWeek,agendaDay'
            },

            'eventSources': self.calEventSources(),
            'weekends': 'true',
            'defaultView': 'agendaDay',
            'height': 800
        })
