from django.conf.urls import patterns, url

from contact import views

urlpatterns = [
    url(r'^$', views.contact, name='contact'),
]
