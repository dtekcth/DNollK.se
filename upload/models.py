from django.db import models
from django.core.files.storage import FileSystemStorage

f_storage = FileSystemStorage(location='/static/photos')

class Upload(models.Model):
    photo = models.ImageField(storage=f_storage)

