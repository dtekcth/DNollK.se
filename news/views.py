# Django modules
from django.http import HttpResponse
from django.shortcuts import render

# Our own modules
from news.models import Post

# Import our paginated_index
from dnollkse.views import paginated_index

"""
news.views module.

This module contains the logic for the views that are related
to the posts.
The functions listed in here are either called via patterns in the posts.url
module, or used in such functions.

TODO: Use templates
"""


def index(request):
    """
    Index function, this is called by the / pattern from news.urls
    This means that this function is called on the url http://APP_URL/posts.

    TODO: Use a template to presents the posts
    """
    posts = Post.published_posts().order_by('-pub_date')

    # Render paginated page
    return paginated_news_index(request, posts)


def index_from_year(request, year):
    """
    Shows the posts from the year specified in the year parameter.
    """
    posts = Post.published_posts_by_year(year)

    # Render paginated page
    return paginated_news_index(request, posts)


def index_from_date(request, year, month):
    """
    Shows the posts from a specific day.
    """
    published_posts = Post.by_month(year, month)
    return render(request, 'news/index.dtl', {'items': published_posts})


def paginated_news_index(request, posts):
    """
    Wraps the generic dnollkse.views.paginated_index to a news-specific
    function.
    """
    return paginated_index(request, posts, 'news/index.dtl', 'items')


def item(request, post_id):
    """
    Displays a single post with id post_id.
    Is called by the pattern /$post_id from news.url

    First we need to filter out the unpublished posts in case the requested
    post is not yet published and then we try to get that post.

    If it does not exist we just print 'No such post' as of now.

    TODO: Use a template to present the post
    """
    try:
        post = Post.published_posts().get(id=post_id)
        content = "Posts article: %s<br> %s"
        return HttpResponse(content % (post_id, post.content))
    except Post.DoesNotExist:
        return HttpResponse("No such post")


def latest(request):
    """
    Retrieves the latest published post and prints it
    First we filter out the unpublished posts and then we get the last element.

    If there is no latest post (for instance if there are no published news)
    we print out 'No posts yet!'

    TODO: Use a template to display the latest post
    """
    try:
        latest_post = Post.published_posts().latest('pub_date')
        return HttpResponse("%s <br> %s" % (latest_post.title,
                                            latest_post.content))
    except Post.DoesNotExist:
        return HttpResponse("No posts yet!")


def rss(request):
    """
    Retrieves all posts and renders them in a rss xml fashion.
    """
    posts = Post.published_posts().order_by('-pub_date')
    return render(request, 'news/feed.dtl', {'items': posts})
