from django.shortcuts import render
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
        return render(request,'register.html',{'message':'Registration Success'})
def search(request):
    if request.method == 'POST':
        id = int(request.POST.get('empid'))
        emp = Emp.objects.filter(idno=id)
        if id not in emp and id==None:
            return render(request, 'details.html', {'message': 'Record Not Found'})
        else:
            return render(request,'details.html',{'emp':emp})

    return render(request,'details.html')