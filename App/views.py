from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
import requests
from . models import *

def generateUserName():
    response = requests.get('https://api.api-ninjas.com/v1/randomuser', headers={'X-Api-Key': 'LceLcBA8r2YMy0aBsaw2Uw==8tGk7QJr0FZefb9L'})
    if response.status_code == 200:
        return response.json()['username']
    
def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func

@login_required(login_url='sigin')
def home(request):
    batches=Batch.objects.all()
    data=list()
    for batch in batches:
        data.append({'name':batch.name})
    context={'data':data}
    return render(request,'App/home.html',context=context)

@login_required(login_url='sigin')
def companies(request,year):
    companies=Company.objects.all()
    data=list()
    for company in companies:
        for batch in company.batches.all():
            if batch.name==year:
                data.append({'name':company.name})
    context={'data':data, 'year':year}
    return render(request,'App/company.html',context=context)

@login_required(login_url='signin')
def experience(request,year,company):
    experience=Experience.objects.all()
    data=list()
    for exp in experience:
        if exp.company.name==company and exp.batch.name==year:
            data.append(exp)
    context={'data':data}
    return render(request,'App/experience.html',context=context)

@unauthenticated_user
def signUp(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
            email=request.POST.get('email')
            paswd=request.POST.get('passwd')
            re_passwd=request.POST.get('repasswd')
            if paswd==re_passwd:
                user=authenticate(request,email=email,password=paswd)
                if user is None:
                    user=User.objects.create_user(
                        username=generateUserName(),
                        email=email,
                        password=paswd
                    )
                    login(request,user)
                    return redirect('home')
    return render(request,'App/register.html')  

@unauthenticated_user
def signIn(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            email=request.POST.get('email')
            password=request.POST.get('passwd')
            user=authenticate(request, email=email, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    return render(request, 'App/login.html')

def logoutUser(request):
    logout(request)
    return redirect('home')