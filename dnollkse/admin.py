# Django models
from django.contrib import admin

# Our own models
from dnollkse.models import Config, Document

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


class DocumentAdmin(admin.ModelAdmin):
    """
    Document admin class.

    TODO: Maybe move Documents out of dnollkse and into its own module?
    """
    model = Document
    list_display = ('title', 'body')


admin.site.register(Config, ConfigAdmin)
admin.site.register(Document, DocumentAdmin)
