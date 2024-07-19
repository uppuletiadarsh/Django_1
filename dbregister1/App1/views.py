from django.shortcuts import render
from .models import details

# Create your views here.
def register(request):
    return  render(request,'register.html')
def save(request):
    if request.method== 'POST':
        custid = int(request.POST.get('custid'))
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpsw = request.POST.get('confirm_password')
        gender = request.POST.get('gender')
        qual = request.POST.get('qualification')
        state = request.POST.get('state')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        save1 = details(cid=custid,uname=username,psw=password,cpsw=cpsw,gender=gender,qual=qual,state=state,email=email,phn=phone)
        save1.save()
        return render(request,'register.html',{'message':'Successfull'})
