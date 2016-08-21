from django import template
from django.utils.html import mark_safe

register = template.Library()

@register.simple_tag
def render_image(upload, **kwargs):
    """
    Tag for calling the rendering method on uploads.

    It sends the positional arguments untouched to the `render` method in
    Upload.
    """
    return mark_safe(upload.render(**kwargs))
