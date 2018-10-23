from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.


class Tags(models.Model):
    title = models.CharField(max_length=25)
   
    def __str__(self):
	return self.title
     
class Post(models.Model):
    pub_date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=200,default=None)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    desc = models.TextField() #this is the book description
    doc = models.FileField(upload_to='documents/', default=None,blank=True)
    #uploaded_at = models.DateTimeField(auto_now_add=True,default=None)
    tags = models.ManyToManyField(Tags)

    def publish(self):
 #       self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

