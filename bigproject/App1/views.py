from django.shortcuts import render

# Create your views here.
def header(request):
    return  render(request,'header.html')
def footer(request):
    return  render(request,'footer.html')
def home(request):
    return  render(request,'home.html')
def register(request):
    return  render(request,'register.html')