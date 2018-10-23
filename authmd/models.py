from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	#following details may also be filled, but are not necessary	
	phno = models.CharField(max_length=10, null=True, blank=True)
	email = models.CharField(max_length=100, null=True, blank=True)
	address = models.CharField(max_length=100, null=True, blank=True)
	
	def __str__(self):
		return str(self.user.username)



