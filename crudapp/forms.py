from django import forms 
from . models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
	password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']
		labels = {'email':'Email','first_name':'First_Name','last_name':'Last_name'}