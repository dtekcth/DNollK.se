from django.contrib import admin
from documents.models import Document


class DocumentAdmin(admin.ModelAdmin):
    """
    Document admin class.
    """
    model = Document
    list_display = ('title', 'body')


admin.site.register(Document, DocumentAdmin)
