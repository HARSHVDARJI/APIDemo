from __future__ import unicode_literals

from django.db import models


# Create your models here.

class UserDetails(models.Model):
    fname = models.CharField(max_length=16, null=True)
    lname = models.CharField(max_length=16)
    email = models.EmailField()

    def __str__(self):
        return self.fname

    def __unicode__(self):
        return self.fname
