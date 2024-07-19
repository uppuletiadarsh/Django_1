from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,'login.html')


def message(request):
    if request.method == 'POST':
        a = request.POST.get('uname')
        b = request.POST.get('psw')
        message = {}
        if a == 'venkat' and b == "sathya":
            message['message'] = 'Valid User'
            return render(request, 'login.html', message)
        else:
            message['message'] = "Invalid User"
            return render(request, 'message.html', message)

    return render(request, 'message.html')