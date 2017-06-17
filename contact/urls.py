from django.conf.urls import url

from contact import views

urlpatterns = [
    url(r'^$', views.contact, name='contact'),
]
