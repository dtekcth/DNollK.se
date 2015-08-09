from django.db import models
from django.core.files.storage import FileSystemStorage
from dnollkse import settings

f_storage = FileSystemStorage(location=settings.STATIC_ROOT + "/uploads/")

class Upload(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(storage=f_storage)

    def __str__(self):
        return self.name
