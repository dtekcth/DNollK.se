from django.db import models

class Committee(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.name

class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nick = models.CharField(max_length=200)
    text = models.TextField()
    number = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    position = models.CharField(max_length=50)
    committee = models.ForeignKey(Committee)

    def __str__(self):
        return self.name

    def getByCommittee(com):
        return Member.objects.filter(committee=com)
