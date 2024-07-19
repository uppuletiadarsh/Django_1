from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Details

# Create your views here.
def register(request):
    return  render(request,'register.html')
def save(request):
    if request.method== 'POST':
        empid = int(request.POST.get('empid'))
        ename = request.POST.get('ename')
        password = request.POST.get('password')
        cpsw = request.POST.get('confirm_password')
        gender = request.POST.get('gender')
        lang = request.POST.getlist('Languages')
        state = request.POST.get('state')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        save1 = details(cid=empid,ename=ename,psw=password,cpsw=cpsw,gender=gender,lang=lang,state=state,email=email,phn=phone)
        save1.save()
        return render(request,'register.html',{'message':'Successfull'})
def user_details(request):
    # Retrieve all details from the database
    details = Details.objects.all()
    return render(request, 'details.html', {'details': details})