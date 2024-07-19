from django.shortcuts import render

# Create your views here.
def login(request):

    return render(request,'login.html')
def details(request):
    a = request.GET.get('fname')
    b = request.GET.get('lname')
    c = a+' '+b
    res= {'fullname':c}
    return render(request,'details.html',res)