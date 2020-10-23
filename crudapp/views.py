from django.shortcuts import render
from django.http import HttpResponseRedirect
from . models import UserProfile
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import  User,auth
from django.views.generic import DetailView
from django.views.generic import ListView
from . import forms 
from django.views.generic.edit import CreateView , UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from . import myserializer
from rest_framework import viewsets


def Home(request):
    return render(request,"index.html",{})


def sign_up(request):
	if request.method == 'POST':
		form      = forms.SignUpForm(request.POST)
		email     = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if password1!=password2:
			messages.error(request,"password no match!!! Try again")
			return redirect('/crudapp/registers/')

		elif User.objects.filter(email=email).exists():
			messages.error(request,"Email Allredy Register.. !!Try new One..!")
			return redirect('/crudapp/registers/')

		elif form.is_valid():
			form.save()
			messages.success(request,"Account create successfully! :)\n Now Log In")
			return redirect('/crudapp/signin/')
		else:
			messages.error(request,'Unsuccessful :(.... try again!!!')
			return redirect('/crudapp/registers/')
	else:
		form = forms.SignUpForm()
	return render(request,"signUp.html",{'form':form})



def sign_in(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			messages.success(request,"You loged In successfully!!!")
			return redirect('/crudapp/home')
		else:
			messages.error(request,"invalid username or password")
			return redirect('/crudapp/signin')
	else:
		return render(request,"signIn.html",{})



def log_out(request):
	auth.logout(request)
	messages.success(request,"You Loged Out Successfully !")
	return redirect('/crudapp/home/')




@method_decorator(login_required, name="dispatch")
class ProfileUpdateView(SuccessMessageMixin,UpdateView):
	template_name = 'editProfile.html'
	model  		  = UserProfile
	fields 		  = ['first_name','last_name','profile_pic'] 
	success_url = '/croudapp/home/'
	success_message = "profile updae successfully"




@login_required
def view_profile(request,i_d):
	profile = User.objects.get(pk=i_d)
	alldetail = UserProfile.objects.get(user=profile.id)
	return render(request,'profile.html',{'alldetail':alldetail})




@login_required
def DeleteProfile(request,i_d):
	message_class="alert-success"
	profile = User.objects.get(pk=i_d)
	want_to_delete_item = UserProfile.objects.get(user=profile.id)
	auth.logout(request)
	want_to_delete_item.delete()
	profile.delete()
	messages.success(request,"Profile Delete Successfully :)")
	return redirect('/crudapp/home/')




class ProfileViewSet(viewsets.ModelViewSet):
	queryset = UserProfile.objects.all().order_by('-id')
	serializer_class = myserializer.ProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-id')
	serializer_class = myserializer.UserSerializer
	