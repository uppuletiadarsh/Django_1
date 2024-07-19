from django.shortcuts import render

# Create your views here.
def home(request):
    return  render(request,'home.html')
def login(request):
    return  render(request,'login.html')
def contact(request):
    return  render(request,'contact.html')
def register(request):
    return  render(request,'register.html')
def welcome(request):
    return  render(request,'welcome.html')
def reg(request):
    return  render(request,'welcomelogin.html')



