from django.contrib import admin
from django.forms import ModelForm, TextInput
from documents.models import Document


class DocumentForm(ModelForm):
    """
    Form for editing documents.
    It mainly overrides the title to a textinput field.
    """
    class Meta:
        model = Document
        fields = ('title', 'body')
        widgets = {
            'title': TextInput
        }


class DocumentAdmin(admin.ModelAdmin):
    """
    Document admin class.
    """
    form = DocumentForm
    change_form_template = 'documents/admin/change_form.dtl'


admin.site.register(Document, DocumentAdmin)
