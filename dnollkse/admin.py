# Django models
from django.contrib import admin

# Our own models
from dnollkse.models import Config

"""
dnollkse.admin module

This is the admin module for system-wide stuff.
"""


class ConfigAdmin(admin.ModelAdmin):
    """
    Config admin class.

    TODO: Make this a singleton instance in some way. We are not interested in
    creating more than one, possibly two configs.
    """
    model = Config

admin.site.register(Config, ConfigAdmin)
