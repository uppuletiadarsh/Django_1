from django.shortcuts import render,redirect
from . import forms
from .models import Emp

# Create your views here.
def register(request):
    form = forms.Emp()
    if request.method == 'POST':
        form = forms.Emp(request.POST)
        if form.is_valid():
            a = form.cleaned_data['idno']
            b = form.cleaned_data['name']
            c = form.cleaned_data['sal']
            print('eid:',a)
            print('name:', b)
            print('sal:', c)
    return render(request,'register.html',{'form':form})
def save(request):
    if request.method == 'POST':
        form = forms.Emp(request.POST)
        if form.is_valid():
            a = form.cleaned_data['idno']
            b = form.cleaned_data['name']
            c = form.cleaned_data['sal']
            e1 = Emp(idno=a,name=b,sal=c)
            e1.save()
            return redirect('register')
        
    return render(request, 'register.html', {'form': form})



