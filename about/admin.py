from django.contrib import admin

from .models import Member, Committee

class MemberInline(admin.TabularInline):
    model = Member
    extra = 6

class CommitteeAdmin(admin.ModelAdmin):
    inlines = [MemberInline]

admin.site.register(Committee, CommitteeAdmin)