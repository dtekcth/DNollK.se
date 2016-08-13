from django.conf.urls import url

from events import views

urlpatterns = [
    # Default index url, matches /
    url(r'^$', views.index, name='events'),

    # Events per year url, matches /YYYY/
    url(r'^(?P<year>[0-9]{4})/$', views.index_from_year, name="events_by_year")
]
