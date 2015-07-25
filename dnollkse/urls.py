# Django modules
from django.conf.urls import patterns, include, url
from django.contrib import admin

"""
dnollkse.urls module

This is the project-wide URL mapping module.
As of now, the only application installed and used is the news application.

It matches everything on the pattern http://example.com/news[/something/more]
"""

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dnollkse.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^nyheter/', include('news.urls')),
    url(r'^om/', include('about.urls')),
    url(r'^kontakt/', include('contact.urls')),
    url(r'^faq/', include('faq.urls')),
    url(r'^lankar/', 'dnollkse.views.links', name='links'),
    url(r'^nollenkat/', 'dnollkse.views.nollenkat', name='nollenkat'),
    url(r'^schema/', 'dnollkse.views.schedule', name='schedule'),
    url(r'^dokument/', 'dnollkse.views.documents', name='documents'),
    url(r'^arr/', include('events.urls')),
    url(r'^', include('news.urls')),
)
