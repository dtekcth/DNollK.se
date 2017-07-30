from django.contrib import admin
from django.forms import ModelForm, TextInput
from links.models import Link


class LinkForm(ModelForm):
    """
    Form for editing links.
    It mainly overrides the title to a textinput field.
    """
    class Meta:
        model = Link
        fields = ('title', 'body')
        widgets = {'title': TextInput}


class LinkAdmin(admin.ModelAdmin):
    """
    Link admin class.
    """
    form = LinkForm
    change_form_template = 'links/admin/change_form.dtl'


admin.site.register(Link, LinkAdmin)
