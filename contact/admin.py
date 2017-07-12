from django.contrib import admin

from .models import ContactInfo


class ContactAdmin(admin.ModelAdmin):
    model = ContactInfo


admin.site.register(ContactInfo, ContactAdmin)
