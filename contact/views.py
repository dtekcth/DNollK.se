from django.shortcuts import render

from about.models import Member, Committee

# Create your views here.

def contact(request):
    committee = Committee.objects.get(name="DNollK")
    members = Member.get_by_committee(committee)

    return render(request, "contact/index.dtl", {'members' : members})
