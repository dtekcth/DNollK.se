from django.conf.urls import url

# Our own modules
from news import views

"""
news.urls module

This module contains the URL patterns that map an URL to a function in
our view module.

When an URL matches a pattern the function that is specified after the pattern
is called.

If the pattern contains regex with a capture group the captured content is sent
to the function as a named parameter (for instance on the post pattern, post_id
will capture the element between news and the last / and sending that to the
views.item function,
"""

urlpatterns = [
    # Matches http://example.com/news
    url(r'^$', views.index, name='news'),

    # Matches http://example.com/nyheter/2015
    url(r'^(?P<year>[0-9]{4})/$', views.index_from_year, name="index_by_year"),

    # Matches http://example.com/nyheter/2015/08/18
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.index_from_date, name="index_by_date"),

    # Matches http://example.com/nyheter/id/4
    url(r'^id/(?P<post_id>\d+)/$', views.item, name="post"),

    # Matches http://example.com/nyheter/senaste
    url(r'^senaste/$', views.latest, name="latest"),

    # Matches http://example.com/nyheter/feed.rss
    url(r'^rss.xml$', views.rss, name="rss")
]
