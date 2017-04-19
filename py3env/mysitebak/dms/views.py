from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Permission
from django.http import HttpResponse,HttpResponseRedirect
from .models import User,AuthUser
from .forms import RUserForm,LUserForm
import sys
# Create your views here.


def registview(request):
    if request.method=="POST":
        uf = RUserForm(request.POST)
        if uf.is_valid():
            jobnumber= uf.cleaned_data['job_number']
            username = uf.cleaned_data['name']
            password = uf.cleaned_data['passwd']
            first_name = uf.cleaned_data['first_name']
            last_name = uf.cleaned_data['last_name']
            email = uf.cleaned_data['email']
            is_staff = uf.cleaned_data['is_staff']
            User.objects.create(name=username,first_name=first_name,last_name=last_name,
            passwd = password,job_number=jobnumber,email=email,is_staff=is_staff)
            return HttpResponse("regist success!!")
    else:
       uf = RUserForm()
    return render(request,'dms/regist.html',{'uf':uf})


def loginview(request):
    if request.method=='POST':
        uf = LUserForm(request.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(name=username,passwd=password,is_active="Y")
            if user:
               #response = HttpResponseRedirect('/erp/index')
               #response.set_cookie('username',username,3600)
               #return response
                request.session['username']=username
                return HttpResponseRedirect('/erp/index/')
        else:
            return HttpResponseRedirect('/erp/login/')
    else:
        uf = LUserForm()
    loginpage="dms/login.html"
    return render(request,loginpage,{'uf':uf})


def indexview(request):
    if request.session.get('username') is not None:
       #username = request.COOKIES.get("username",'')
        username = request.session.get('username')
        return render(request,'dms/index.html',{'username':username})
    else:
        return HttpResponseRedirect('/erp/login/')

def logoutview(request):
    response = HttpResponseRedirect('/erp/login/')
    response.delete_cookie('username')
    del request.session['username']
    return response
    #return HttpResponseRedirect("/erp/login/")

