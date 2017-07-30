from django.shortcuts import render as orig_render

from dnollkse.models import Config
from contact.models import ContactInfo

"""
dnollkse.viewHelper module

This is a project-wide helper module for views and template related stuff. It
contains helper functions and methods to ease some of the custom stuff we've
added to templates, such as bundles that should always be sent to the
templates.
"""


def render(request,
           template_name,
           context=None,
           content_type=None,
           status=None,
           using=None):
    newContext = {'config': Config.objects.all()[0],
                  'contact': ContactInfo.objects.all()[0]}
    # Merge the context from argument with the base context
    newContext.update(context)

    # Return a call to the original method
    return orig_render(request,
                       template_name,
                       newContext,
                       content_type,
                       status,
                       using)
