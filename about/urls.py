from django.conf.urls import patterns, url

from about import views

urlpatterns = patterns('',
    # Matches http://example.com/about
    url(r'^$', views.index, name='index'),

    # Matches http://example.com/about/dnollk
    url(r'^dnollk/$', views.dnollk, name="dnollk"),

    # Matches http://example.com/about/foreningar
    url(r'^foreningar/$', views.foreningar, name="foreningar"),

    # Matches http://example.com/about/karen
    url(r'^karen/$', views.karen, name="karen"),
)
