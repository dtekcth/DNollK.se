#!/usr/bin/env python

from django.db import models


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
    year = models.IntegerField()

    # Social widgets
    instagram_widget_url = models.TextField()
    twitter_widget_id = models.TextField()

    # Calendar
    gcal_api_key = models.TextField()
    gcal_dnollk_calendar_id = models.TextField()

    # Not in use atm
    gcal_timeedit_calendar_id = models.TextField()
