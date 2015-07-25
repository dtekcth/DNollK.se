from django.conf.urls import patterns, url

from arr import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='events'),
)
