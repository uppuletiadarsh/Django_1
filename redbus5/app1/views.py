from django.shortcuts import render

# Create your views here.
def table(request):
    details={'caption':'EMPLOYEE DETAILS','id':101,'name':'ADARSH','salary':'65000'}
    return render(request,'table.html',details)
