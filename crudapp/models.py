from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(to = User,on_delete = models.CASCADE)
	first_name = models.CharField(max_length = 30,null=True,blank=True)
	last_name = models.CharField(max_length = 30,null=True,blank=True)
	profile_pic = models.ImageField(upload_to = 'profilePic//',null=True,blank=True)
	email = models.EmailField(null=True,blank=True)
	def __str__(self):
	 return self.user


# https://app.getpostman.com/join-team?invite_code=600f6414134145c3e6bd97148863d545