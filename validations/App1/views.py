from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')
def valid(request):
    a =request.POST.get('uname')
    b =request.POST.get('psw')
    c=a+' '+b
    res={'res':c}
    if a=='venkat' and b=='sathya':
        return render(request,'valid.html',res)
    else:
        return render(request, 'invalid.html')


