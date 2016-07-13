# System libraries
from datetime import date
from django.db import models

# Application-wide settings
from dnollkse import settings

"""
uploads.models module.

In this moduel we define the model for our uploaded files.
The only special things here are the functions used to ensure that the files are
saved in a easy-to-access location.
"""

def setFilePath(instance, filename):
    """
    Creates the base directory where we save the image.
    It is saved in STATIC_ROOT/uploads/YYYY/
    """
    year = date.today().year
    ext = instance.name.split('.')[-1]

    return '/'.join([settings.STATIC_ROOT, 'uploads', str(year), filename])

class Upload(models.Model):
    """
    Upload model.

    Represents an uploaded image with a name and image field.
    The image is stored on disk as STATIC_ROOT/uploads/YYYY/name.ext.
    """
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=setFilePath)

    def __str__(self):
        """
        Overrides the default __str__ (ToString equivalent in other languages)
        with a function that returns the name of the upload.
        """
        return self.name

    def save(self, *args, **kwargs):
        """
        Overrides the save function to save the file where we want.
        It is saved with the name of the upload as the image filename.
        """
        fileName = self.photo.name.split('/')[-1]
        ext = fileName.split('.')[-1]
        self.photo.name = self.name + '.' + ext
        super(Upload, self).save(*args, **kwargs)

    @staticmethod
    def route(uploadName):
        """
        Takes a string matching the name of an upload and
        returns the path to that upload's image.

        Might be used in routing in a relatively close feature.
        """
        u = Upload.objects.get(name=uploadName)
        return u.photo.name
