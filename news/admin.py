# Django models
from django.contrib import admin

# Our own modules
from news.models import Post

"""
news.admin module

This is the admin module for our news application. Here we can define admin
classes for our models and customize how they appear in the admin interface.
"""


class PostAdmin(admin.ModelAdmin):
    """
    Post admin class.

    We define that the model that we handle is Post and that we want to
    display the title, publish date, author and whether the post has been
    published. List_diplay make these fields visible in the post overview.

    List_filter makes the fields filterable, with predefined options for the
    different fields.
    """
    model = Post
    list_display = ('title', 'pub_date', 'author', 'published')
    list_filter = ['pub_date', 'published']
    change_form_template = 'news/admin/change_form.html'


# Register the models in our admin view
admin.site.register(Post, PostAdmin)
