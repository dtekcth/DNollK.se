from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateTimeField('datum')
    text = models.TextField()

    def __str__(self):
        return self.name
