from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

"""
dnollkse.views module

This is the project-wide views module.
It contains views that are not placed in their own applications yet.
"""


def home(request):
    """
    Index function of the project.
    Displays a dummy page.
    """
    return render(request, "dnollkse/home.dtl", {})


def nollenkat(request):
    """
    Renders the page to the nollenkät.
    """
    return render(request, "dnollkse/nollenkat.dtl", {})


def schedule(request):
    """
    Renders schedule page.
    """
    return render(request, "dnollkse/schedule.dtl", {})


def links(request):
    """
    Renders page with important links and such.
    """
    return render(request, "dnollkse/lankar.dtl", {})


def documents(request):
    """
    Renders page with links to documents.
    """
    return render(request, "dnollkse/documents.dtl", {})


def paginated_index(request, items, template, items_name):
    """
    Paginated index function, this is called by other views to create a
    paginated page.

    This function expects a request object, a list of items, a template on
    which it will render a batch of the items based on the parameters in
    the querydict (retrieved by GET) in the request object and the name of
    the of the variable it should send items as.
    """
    # Take parameters from querystring we're interested in.
    count = request.GET.get('antal', 10)
    page = request.GET.get('sida', 1)

    paginator = Paginator(items, count)

    # Try set the context to a paginated page.
    try:
        context = {items_name: paginator.page(page)}
    except PageNotAnInteger:
        context = {items_name: paginator.page(1)}
    except EmptyPage:
        context = {items_name: paginator.page(paginator.num_pages)}

    return render(request, template, context)
