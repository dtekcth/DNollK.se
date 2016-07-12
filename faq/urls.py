from django.conf.urls import include, url
from django.contrib import admin

from faq import views

urlpatterns = [
    url(r'^$', views.faq, name='faq'),
]
