from django.db import models


# Create your models here.
class ContactInfo(models.Model):
    phone = models.CharField(10)
    mail = models.EmailField()
    address = models.TextField()
    union_phone = models.CharField(10)
    student_counselor_dtek = models.CharField(10)
    curator = models.CharField(10)
    chalmers_ward = models.CharField(10)
    healthcare_info = models.CharField(10)
    emergency_info = models.CharField(10)
