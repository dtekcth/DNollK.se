# Django modules
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# Import dnollkse views
from . import views
from documents import views as document_views
from links import views as links_views

"""
dnollkse.urls module

This is the project-wide URL mapping module.
To add a new app we have to specify a route to it in the urlpatterns.

The base address of the server is assumed to be http://example.com

The apps installed as of 2016-01-04 is:
app:     ->   url
admin:   ->   http://example.com/admin
news:    ->   http://example.com/nyheter
about:   ->   http://example.com/om
contact: ->   http://example.com/kontakt
faq:     ->   http://example.com/faq
events:  ->   http://example.com/arr

In the url objects we see that we include the url modules from every app and
this is where we define each app-specific route.

Beside the apps there are url objects where the second field starts with views
and these all points to view-methods inside main app, dnollkse.
These views are defined in views.py.
"""

urlpatterns = [
    # Examples:
    # url(r'^$', 'dnollkse.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^nyheter/', include('news.urls')),
    url(r'^om/', include('about.urls')),
    url(r'^kontakt/', include('contact.urls')),
    url(r'^faq/', include('faq.urls')),
    url(r'^lankar/', links_views.index, name='links'),
    url(r'^nolldeklaration/', views.nollenkat, name='nollenkat'),
    url(r'^schema/', views.schedule, name='schedule'),
    url(r'^dokument/', document_views.index, name='documents'),
    url(r'^arr/', include('events.urls')),
    url(r'^', include('news.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
