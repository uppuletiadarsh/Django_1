from django.shortcuts import render

# Create your views here.
def showindex(request):
    data={'a':15,'b':22,'c':18}
    return  render(request,'index.html',data)
