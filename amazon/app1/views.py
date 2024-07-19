from django.http import HttpResponse

def aboutus(request):
    return HttpResponse('<h1>welcome to django first app</h1>')

def register(request):
    return HttpResponse('<h1>welcome to register</h1>')
