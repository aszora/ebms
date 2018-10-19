from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    pub_date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    desc = models.TextField() #this is the book description

    def publish(self):
 #       self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

