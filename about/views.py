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
    committees = Committee.objects.all().exclude(name="DNollK")
    f = {}
    for com in committees:
        f[com] = Member.getByCommittee(com)
    
    return render(request, "about/foreningar.dtl", {'committees' : committees, 'members_dict' : f})

def brage(request):
    return render(request, "about/brage.dtl", {})