from django.shortcuts import render,redirect
from .models import Emp

# Create your views here.
def register(request):
    return render(request,'register.html')
def save(request):
    if request.method == 'POST':
        eid = int(request.POST.get('eid'))
        ename = (request.POST.get('ename'))
        sal = int(request.POST.get('sal'))
        e1 = Emp(idno=eid,name=ename,salary=sal)
        e1.save()
        return redirect('details')
def details(request):
    # Retrieve all details from the database
    details = Emp.objects.all()
    return render(request, 'details.html', {'details': details})
def delete(request,id):
    id = Emp.objects.get(idno=id)
    id.delete()
    return redirect('details')
def update(request,id):
    res =  Emp.objects.get(idno=id)
    return render(request,'update.html',{'res':res})
def updated(request,id):
    a = request.POST.get('eid')
    b = request.POST.get('ename')
    c = request.POST.get('sal')
    update = Emp.objects.get(idno=id)
    update.idno = a
    update.name = b
    update.salary = c
    update.save()
    return redirect('details')
