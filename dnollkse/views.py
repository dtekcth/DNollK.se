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
