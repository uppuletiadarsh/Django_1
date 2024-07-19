from django.shortcuts import render, redirect
from . import forms
from .models import Register

from django.shortcuts import render, redirect
from . import forms
from .models import Register

def register(request):
    if request.method == 'POST':
        form = forms.Register(request.POST)
        if form.is_valid():
            a = form.cleaned_data['FirstName']
            b = form.cleaned_data['LastName']
            c = form.cleaned_data['Email']
            d = form.cleaned_data['UserName']
            e = form.cleaned_data['PassWord']
            j = form.cleaned_data['ConfirmPassword']
            f = form.cleaned_data['Gender']
            g = form.cleaned_data['Phone']
            e1 = Register(FirstName=a,LastName=b,Email=c,UserName=d,PassWord=e,ConfirmPassword=j,Gender=f,Phone=g)
            e1.save()
            return redirect('register')
    else:
        form = forms.Register()
    return render(request, 'register.html', {'form': form})
