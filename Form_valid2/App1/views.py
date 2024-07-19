from django.shortcuts import render,redirect
from . import forms
from . models import Emp
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = forms.EmpReg(request.POST)
        if form.is_valid():
            a = form.cleaned_data['Id']
            b = form.cleaned_data['Name']
            c = form.cleaned_data['PassWord']
            d = form.cleaned_data['ConfirmPassword']
            e = form.cleaned_data['Dept_Id']
            Employee = Emp(Id=a,Name=b,PassWord=c,ConfirmPassword=d,Dept_Id=e)
            Employee.save()
            return redirect('register')
    else:
        form = forms.EmpReg()
    return render(request, 'register.html', {'form': form })

def search(request):
    return render(request,'search.html')
def searchElement(request):
    if request.method == 'POST':
        id = request.POST.get('dept')
        try:
            det = Emp.objects.filter(Dept_Id=id)
            return render(request, 'search.html', {'res': det})
        except Emp.DoesNotExist:
            return render(request, 'search.html')
    return render(request, 'search.html')