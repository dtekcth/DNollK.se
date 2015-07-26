from django.contrib import admin

from .models import Faq

class FaqAdmin(admin.ModelAdmin):
    """
    FAQ admin class.

    We define that the model that we handle is Faq and that we want to change the form to use django_wysiwyg.
    """
    model = Faq
    change_form_template = 'faq/admin/change_form.html'

admin.site.register(Faq, FaqAdmin)
