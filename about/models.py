from django.db import models

class Committee(models.Model):
    """
    The db model for a Committee. Choosing an image and description text is optional.
    """
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='%Y', blank=True) # Upload to subfolder of %MEDIA_ROOT named after current year
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    """
    The db model for a member of a committee. Optional fields are description text, phone number, nickname and image.
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nick = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True)
    number = models.CharField(max_length=50, blank=True)
    image = models.FileField(upload_to='%Y', blank=True)  # Upload to subfolder of %MEDIA_ROOT named after current year
    position = models.CharField(max_length=50)
    committee = models.ForeignKey(Committee)

    def __str__(self):
        return self.get_full_name_with_nick()

    def get_by_committee(com):
        return Member.objects.filter(committee=com)

    def get_full_name(self):
        return self.first_name +  " " + self.last_name

    def get_full_name_with_nick(self):
        return self.first_name + " \"" + self.nick + "\" " + self.last_name
