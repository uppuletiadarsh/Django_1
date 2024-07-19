from django.shortcuts import render
from .models import emp

# Create your views here.
def register(request):
    return render(request,'register.html')
def save(request):
    if request.method == 'POST':
        eid = int(request.POST.get('eid'))
        ename = (request.POST.get('ename'))
        sal = int(request.POST.get('sal'))
        e1 = emp(idno=eid,name=ename,salary=sal)
        e1.save()
        return render(request,'register.html',{'message':'Registration Success'})
