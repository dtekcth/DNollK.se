from django.shortcuts import render
from django.http import HttpResponse

from about.models import Committee, Member

def dnollk(request):
    committee = Committee.objects.get(name="DNollK")
    members = Member.get_by_committee(committee)
    return render(request, "about/dnollk.dtl", {'committee' : committee, 'members' : members})

def index(request):
    return render(request, "about/index.dtl", {})

def sektionen(request):
    committees = Committee.objects.all().exclude(name__startswith="DNollK")
    f = {}
    for com in committees:
        f[com] = Member.get_by_committee(com)
    
    return render(request, "about/sektionen.dtl", {'committees' : committees, 'members_dict' : f})

def brage(request):
    return render(request, "about/brage.dtl", {})

def donk(request):
    committees = Committee.objects.filter(name__startswith="DNollK-").order_by("-name")
    f = {}
    for com in committees:
        f[com] = Member.get_by_committee(com)
    
    return render(request, "about/donk.dtl", {'committees' : committees, 'members_dict' : f})
