# Django modules
from django.contrib import admin

# Our own modules
from events.models import Event

"""
events.admin module

This is the admin module for our events application.
Here we can define admin classes for our models and customize how they appear in the admin interface.
"""

class EventAdmin(admin.ModelAdmin):
    """
    Event admin class.

    We define that the model that we handle is Event and that we want to change the form to use django_wysiwyg.
    """
    model = Event
    change_form_template = 'events/admin/change_form.html'

# Register the models in our admin view
admin.site.register(Event, EventAdmin)
