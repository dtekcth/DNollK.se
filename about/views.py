from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from about.models import Committee, Member

import collections

def dnollk(request):
    """
    Retrieves the "latest" Committee (with its members) with a name starts
    with DNollK and uses them as parameters in "about/dnollk.dtl" template.

    For instance: Given that the database contains two committees with names
    starting with DNollK: DNollK-2014 and DNollK-2015.
    In this case it will retrieve DNollK-2015 as its name is considered as
    "bigger" than DNollK-2014.
    """
    committee = Committee.objects.filter(name__startswith="DNollK").order_by('-name')[0]
    members = Member.get_by_committee(committee)
    return render(request, "about/dnollk.dtl", {'committee' : committee, 'members' : members})

def index(request):
    """
    Renders the index template without any paramters.
    """
    return render(request, "about/index.dtl", {})

def sektionen(request):
    """
    Retrieves all committees except the ones with names matching DNollK and
    uses them as parameters in "about/sektionen.dtl" template.

    The intention with this view and it template is to present the committees
    off the student union division that are active the current year and it will
    not try to distinguish the committees or order them by year.
    If two committees exists from different years, both will be presented.
    """
    committees = Committee.objects.all().exclude(name__startswith="DNollK")
    f = {}
    for com in committees:
        f[com] = Member.get_by_committee(com)

    return render(request, "about/sektionen.dtl", {'committees' : committees, 'members_dict' : f})

def brage(request):
    """
    Presents Brage in all his glory and might!
    """
    return render(request, "about/brage.dtl", {})

def donk(request):
    """
    Retrieves all committees with names starting with DNollK and orders them
    by name in a descending fashion.

    These committees and their members are then used as parameters to
    "about/donk.dtl template".
    """
    committees = Committee.objects.filter(name__startswith="DNollK-").order_by("-name")
    f = {}
    for com in committees:
        f[com] = Member.get_by_committee(com)

    d = collections.OrderedDict(sorted(f.items(),key=lambda t: str(t[0]), reverse=True))

    return render(request, "about/donk.dtl", {'committees' : committees, 'members_dict' : d})
