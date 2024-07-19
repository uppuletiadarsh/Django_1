from django.shortcuts import render

# Create your views here.
def index(request):
    student={'id':1122,'name':'Adarsh','desg':'Developer'}
    return render(request,'index.html', student)