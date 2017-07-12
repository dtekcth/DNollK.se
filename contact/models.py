from django.db import models


# Create your models here.
class ContactInfo(models.Model):
    phone = models.CharField(max_length=10)
    mail = models.EmailField()
    address = models.TextField()
    union_phone = models.CharField(max_length=10)
    student_counselor_dtek = models.CharField(max_length=10)
    curator = models.CharField(max_length=10)
    chalmers_ward = models.CharField(max_length=10)
    healthcare_info = models.CharField(max_length=10)
    emergency_info = models.CharField(max_length=10)
