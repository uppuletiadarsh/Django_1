from django.shortcuts import render,redirect

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
             return redirect('welcome')
         else:
             return redirect('login')
    return render(request,'welcome.html')