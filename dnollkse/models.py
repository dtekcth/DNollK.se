#!/usr/bin/env python

from django.db import models
import json


class Document(models.Model):
    title = models.TextField()
    body = models.TextField()

    def render(self):
        html = ["<div class=\"card center-text\">",
                "<h4><i>" + self.title + "</i></h4>",
                "<p>" + self.body + "</p>",
                "</div>"]

        return "\n".join(html)

    def __str__(self):
        return self.title


class Config(models.Model):
    # Social widgets
    instagram_widget_url = models.TextField()
    twitter_widget_id = models.TextField()

    # Calendar
    gcal_api_key = models.TextField()
    gcal_dnollk_calendar_id = models.TextField()
    gcal_dnollk_calendar_url = models.TextField()
    gcal_timeedit_calendar_id = models.TextField()
    gcal_asp_calendar_id = models.TextField()

    enable_dnollk_calendar = models.BooleanField()
    enable_timeedit_calendar = models.BooleanField()
    enable_asp_calendar = models.BooleanField()

    # Form
    gform_link = models.TextField()
    gform_embed_link = models.TextField()

    enable_form = models.BooleanField()

    def calEventSources(self):
        """
        Returns a python object with the event sources used in FullCalender.
        """
        eventSources = []
        if self.enable_dnollk_calendar:
            eventSources.append({
                'googleCalendarId': self.gcal_dnollk_calendar_id,
                'className': 'eventCalendar',
                'color': "#FA6607"
            })

        if self.enable_timeedit_calendar:
            eventSources.append({
                'googleCalendarId': self.gcal_timeedit_calendar_id,
                'className': 'schoolCalendar',
                'color': 'CornFlowerBlue'
            })

        if self.enable_asp_calendar:
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
