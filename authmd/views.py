#from .models import Post
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
	response = {}
	if request.method == 'POST' :
		username = request.POST['username']
		password = request.POST['password']
		if User.objects.filter(username=username):
			response['error']=1
		else:
			
			User.objects.create_user(username = username,password = password,email='')
	return render(request,'authmd/login.html',response)



def signin(request):
	response = {}
	if request.method == 'POST' :
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is None :
			response['error']=2
			return render(request,'authmd/login.html',response)
		else :
			login(request,user)
			return redirect('/authmd')
	return render(request,'authmd/login.html',response)
