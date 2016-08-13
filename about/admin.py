from django.contrib import admin

from .models import Member, Committee

class MemberInline(admin.StackedInline):
    model = Member
    extra = 1

class CommitteeAdmin(admin.ModelAdmin):
    """
    Committee admin class.

    We define that the model we use is Committee, that members are editied inline with the committee and that we want to be able to use django_wysiwyg.
    """
    model = Committee
    change_form_template = 'about/admin/change_form.html'
    inlines = [MemberInline]

admin.site.register(Committee, CommitteeAdmin)
