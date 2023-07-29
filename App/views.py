from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from . models import *
from . helper import *
from . forms import *
    
@login_required(login_url='sigin')
def home(request):
    companies=Company.objects.all()
    data=list()
    for comp in companies:
        data.append(comp)
    context={'data':data}
    return render(request,'App/home.html',context=context)

@login_required(login_url='sigin')
def companies(request,name):
    comp=Company.objects.get(name=name)
    batches=comp.batches.all()
    data=list()
    for batch in batches:
        data.append(batch)
    print(data)
    context={'data':data, 'comp':comp}
    return render(request,'App/company.html',context=context)

@login_required(login_url='signin')
def experience(request,name,year):
    experience=Experience.objects.all()
    data=list()
    for exp in experience:
        if exp.company.name==name and exp.batch.name==year:
            data.append(exp)
    context={'data':data,'condition':'Yes'}
    return render(request,'App/experience.html',context=context)

@login_required(login_url='signin')
@superuser_required
def unverified(request):
    experience=Experience.objects.all()
    data=list()
    for exp in experience:
        if exp.verified=="No":
            data.append(exp)
    context={'data':data,'condition':'No'}
    return render(request,'App/experience.html',context=context)

@superuser_required
def verify(request,id):
    experience=Experience.objects.get(id=id)
    experience.verified='Yes'
    experience.save()
    return redirect('unverified')

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
                        password=paswd,
                    )
                    img=generateUserAvatar(user.username)
                    user.profile.save(f"{user.id}.png",img,save=True)
                    user.save()
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

@superuser_required
def exp_add(request):
    form = experienceForm()
    if request.method == "POST":
        form = experienceForm(request.POST)
        if form.is_valid():
            form.save()
            current_year = str(form.cleaned_data['batch'])
            company = form.cleaned_data['company']
            return redirect('experience', name=company, year=current_year[5:])
            
            # return redirect(f'exp/{company}/{year[5:]}/')
    context = {"form": form}
    return render(request, "App/experience_crud.html", context)

@superuser_required
def exp_update(request, pk):
    experience = Experience.objects.get(id=pk)
    form = experienceForm(instance=experience)
    if request.method == "POST":
        form = experienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            current_year = str(form.cleaned_data['batch'])
            company = form.cleaned_data['company']
            return redirect('experience', name=company, year=current_year[5:])
    context = {"form": form, "experience": experience}
    return render(request, "App/experience_crud.html", context)

@superuser_required   
def exp_delete(request, pk):
    experience = Experience.objects.get(id=pk)
    # current_year = experience.batch.name
    # company = experience.company.name
    
    if request.method == "POST":
        current_year = str(experience.batch.name)
        company = experience.company.name
        # print(type(current_year), company )
        experience.delete()
        # print("fefafagagag")
        # print(current_year, company)
        return redirect('experience', name=company, year=str(current_year))
    context = {"experience":experience}
    return render(request, "App/delete.html", context)