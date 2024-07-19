from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def logout(request):
    return render(request,'logout.html')
def welcome(request):
    if request.method=='POST':
         a = request.POST.get('uname')
         b = request.POST.get('psw')
         if (a == 'venkat' and b == 'venkat'):
             return render(request,'welcome.html')
         else:
             return render(request, 'login.html')
    return render(request, 'welcome.html')