from django.shortcuts import render

# Create your views here.
def showindex(request):
    data={'marks':[50,60,70]}
    return render(request,'index.html',data )
