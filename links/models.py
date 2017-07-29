from django.db import models

# Create your models here.
class Link(models.Model):
    title = models.TextField()
    body = models.TextField()
