from django.shortcuts import render

# Create your views here.
def calc(request):
    if request.method == 'POST':
        a = eval(request.POST.get('asal'))
        b = a/12
        sal = {'msal':b, 'asal':a}
        return render(request, 'salary.html',sal)
    else:
        return render(request,'salary.html')
