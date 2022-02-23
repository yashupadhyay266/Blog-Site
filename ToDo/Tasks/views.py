import re
from django.shortcuts import render,redirect
from Tasks.models import Task,ImageFromUser
import math

from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='Tasks:login')
def base(request):

    if request.method=='POST':
        imageuser=request.user
       
        caption=request.POST.get('caption')
        imagedescription=request.POST.get('imagedescription')
        image_uploaded=request.FILES.get('image_upload')
       
        instance=ImageFromUser.objects.create(imageuser=imageuser,caption=caption,imagedescription=imagedescription,image_uploaded=image_uploaded)
        instance.save()
    context={}
    return render(request,'main.html',context)

def showimage(request):
    getimages=ImageFromUser.objects.filter(imageuser=request.user).order_by('-date_uploaded')
    context={'getimages':getimages}
    return render(request,'image.html',context)


def deleteallimages(request):
    
    ImageFromUser.objects.all().delete() 
   
    return redirect('Tasks:base')



@login_required(login_url='/')
def home(request):
   
    context={'success':False,'oncesubmitted':False}
    if request.method=='POST':
        taskuser=request.user
        taskid=len(Task.objects.all())+1
        title=request.POST['tasktitle']
        description=request.POST['taskdescription']

        instance=Task.objects.create(taskuser=taskuser,tasktitle=title,taskdescription=description,task_id=taskid)
        instance.save()
     
        
        context={'success':True,'oncesubmitted':True}
    return render(request,'home.html',context)

@login_required(login_url='/')
def taskslist(request):
    no_of_items=4
    page_no=int(request.GET.get('page',1))
    length=len(Task.objects.all())
    lop=length
    if lop==0:
        lop=True
    else:
        lop=False
    alltasks=Task.objects.filter(taskuser=request.user).values()[(page_no-1)*no_of_items:page_no*no_of_items]
    if page_no>1:
        prev=page_no-1
    else:
        prev=None
    if page_no<length/no_of_items:
        nxt=page_no+1
    else:
        nxt=None
    maximum_pages=math.ceil(length/no_of_items)
    pagenumbered=1
    context={'tasksgiven' : alltasks,'prev':prev,'nxt':nxt,'no_of_items':no_of_items,'maximum_pages':range(maximum_pages),'pagenumbered':pagenumbered,'lop':lop}
    return render(request,'tasklist.html',context)   


def displayall(request):
    alltasks=Task.objects.filter(taskuser=request.user).values()
    context={'tasksgiven':alltasks}
    return render(request,'displayall.html',context)   



def update(request,name):
    itemname=Task.objects.get(tasktitle=name)
    context={'name':name}
    if request.method=='POST':

        itemname.tasktitle=request.POST['tasktitle']
        itemname.taskdescription=request.POST['taskdescription']
        itemname.save()
      
        return redirect('Tasks:displayall')
    
    return render(request,'update.html',context)


def delete(request,name):
    itemname=Task.objects.get(tasktitle=name)
    itemname.delete()
    return redirect('Tasks:taskslist')

def deleteall(request):
    
    Task.objects.all().delete() 
    l=len(Task.objects.all())
    request.session['deleted']=True
    request.session['lp']=l
    return redirect('Tasks:taskslist')

def registerPage(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
    if form.is_valid():
        user=form.save()
        username=form.cleaned_data.get('username')
        messages.success(request,'Account is Created Sucessfully!!'+username)
        return redirect('Tasks:login')
    context={'form':form}
    return render(request,'register.html',context)

def loginPage(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
    
        if user is not None:
            login(request,user)
            return redirect('Tasks:base')
        if user is None:
            messages.success(request,'Username or Password is Incorrect !!')
       
    context={}
    return render(request,'login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('Tasks:login')



def passwordreset(request):
    if request.method=='POST':
        username=request.POST.get('username')
        u=User.objects.get(username=username)
        newpassword=request.POST['newpassword']
        u.set_password(newpassword)
        u.save()
        return redirect('Tasks:login')
   
    return render(request,'passwordreset.html')

