# Django modules
from django.shortcuts import render
from django.http import HttpResponse

# Our own modules
from news.models import Author, Post

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

    allPublishedPosts = Post.publishedPosts()
    return HttpResponse("Index of posts application")

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
        post = Post.publishedPosts().get(id=post_id)
        content = "Posts article: %s<br> %s"
        return HttpResponse(content % (post_id,post.content))
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
        latestPost = Post.publishedPosts().latest('pub_date')
        return HttpResponse("%s <br> %s" % (latestPost.title, latestPost.content))
    except Post.DoesNotExist:
        return HttpResponse("No posts yet!")
