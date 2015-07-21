from django.conf.urls import patterns, include, url
from django.contrib import admin

from faq import views

urlpatterns = patterns('',
    url(r'^$', views.faq, name='faq'),
)