from django.contrib import admin

from .models import Upload

"""
upload.admin module.

This is hte admin module for our upload application.
Here the admin class for the Upload model is defined and customizes the
appearance in the admin interface.
"""

class UploadAdmin(admin.ModelAdmin):
    """
    Upload admin class.

    Contains filter properties and what templates that should be active.
    """
    model = Upload
    list_display = ('name', 'photo')
    exclude = ['date_uploaded']
    list_filter = ['date_uploaded']

admin.site.register(Upload, UploadAdmin)
