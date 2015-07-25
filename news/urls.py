from django.conf.urls import patterns, url

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

urlpatterns = patterns('',
    # Matches http://example.com/news
    url(r'^$', views.index, name='news'),

    # Matches for example http://example.com/news/4
    url(r'^(?P<post_id>\d+)/$', views.item, name="post"),

    # Matches http://example.com/news/latest
    url(r'^latest/$', views.latest, name="latest"),

    # Matches http://example.com/news/feed.rss
    url(r'^rss.xml$', views.rss, name="rss"),
)
 
