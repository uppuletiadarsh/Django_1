from django.shortcuts import render,redirect
from .models import Insert
# Create your views here.
def insert(request):
    return render(request,'insert.html')
def save(request):
   if request.method == "POST":
       id = int(request.POST.get('id'))
       name = request.POST.get('name')
       dept = request.POST.get('dept')
       E1 = Insert(id=id,name=name,dept=dept)
       E1.save()
       message = "Record Inserted"
       return render(request,'insert.html',{'message':message})
   return render(request,'insert.html')
def Details(request):
    details = Insert.objects.all()
    return render(request,'details.html',{'det':details})
def delete(request,id):
    details = Insert.objects.get(id=id)
    details.delete()
    return redirect('details')
def update(request,id):
    details = Insert.objects.get(id=id)
    return render(request,'update.html',{'det':details})
def updated(request,id):
    details = Insert.objects.get(id=id)
    id = request.POST.get('id')
    name = request.POST.get('name')
    dept = request.POST.get('dept')
    details.id = id
    details.name = name
    details.dept = dept
    details.save()
    return redirect('details')

