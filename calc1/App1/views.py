from django.shortcuts import render

# Define your view functions here

def form(request):
    return render(request, 'operations.html')

def calc1(request):
    if request.method == 'POST':
        a = eval(request.POST.get('a'))
        b = eval(request.POST.get('b'))
        result = a + b
        add = {'add': result,'a':a,'b':b}
        return render(request, 'operations.html',add )
    else:
        return render(request, 'operations.html')

def calc2(request):
    if request.method == 'POST':
        a = eval(request.POST.get('a'))
        b = eval(request.POST.get('b'))
        result = a - b
        sub = {'sub': result,'a':a,'b':b}
        return render(request, 'operations.html',sub)
    else:
        return render(request, 'operations.html')

def calc3(request):
    if request.method == 'POST':
        a = eval(request.POST.get('a'))
        b = eval(request.POST.get('b'))
        result = a * b
        mul = {'mul': result,'a':a,'b':b}
        return render(request, 'operations.html', mul)
    else:
        return render(request, 'operations.html')

def calc4(request):
    if request.method == 'POST':
        a = eval(request.POST.get('a'))
        b = eval(request.POST.get('b'))
        if b != 0:
            result = a / b
            div = {'div': result,'a':a,'b':b}
            return render(request, 'operations.html',div)
        else:
            return render(request, 'operations.html')
    else:
        return render(request, 'operations.html')