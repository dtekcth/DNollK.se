from django.shortcuts import render
from django.http import HttpResponse

from about.models import Committee, Member

def dnollk(request):
    committee = Committee.objects.get(name="DNollK")
    members = Member.getByCommittee(committee)
    return render(request, "about/dnollk.dtl", {'committee' : committee, 'members' : members})

def index(request):
    return render(request, "about/index.dtl", {})

def foreningar(request):
    return HttpResponse("Föreningar")

def karen(request):
    return HttpResponse("Kåren")
