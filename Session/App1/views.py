from django.shortcuts import render,redirect
from .models import student

# Create your views here.
def basic(request):
    return  render(request,'basic.html')
def education(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    fname = request.POST.get('fname')
    request.session['name'] = name
    request.session['email'] = email
    request.session['fname'] = fname
    return render(request,'education.html')
def experience(request):
    college = request.POST.get('college')
    branch = request.POST.get('branch')
    pin = request.POST.get('pin')
    request.session['college'] = college
    request.session['branch'] = branch
    request.session['pin'] = pin
    return render(request, 'experience.html')
def details(request):
    company = request.POST.get('company')
    experience = request.POST.get('exp')
    role = request.POST.get('role')
    request.session['company'] = company
    request.session['role'] = role
    request.session['experience'] = experience
    a = request.session['name']
    b = request.session['email']
    c = request.session['fname']
    d = request.session['college']
    e = request.session['branch']
    f = request.session['pin']
    g = request.session['company']
    h = request.session['role']
    i = request.session['experience']
    details = {'name': a , 'email':b ,'fname': c, 'college':d ,'branch':e,'pin':f,'company':g,'role':h,'experience':i}
    return render(request, 'details.html',details)
def save(request):
    a = request.session['name']
    b = request.session['email']
    c = request.session['fname']
    d = request.session['college']
    e = request.session['branch']
    f = request.session['pin']
    g = request.session['company']
    h = request.session['role']
    i = request.session['experience']
    save = student(name=a,email=b,father_name=c,college=d,branch=e,pin=f,company=g,role=h,experience=i)
    save.save()
    request.session.flush()
    return render(request,'details.html')

def applicationsccs(request):
    return render(request,'complete.html')