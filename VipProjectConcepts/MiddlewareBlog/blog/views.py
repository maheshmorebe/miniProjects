from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    print("I am home")
    return HttpResponse("This is home page")

def excep(request):
    print("I am exception view...")
    a = 10/0
    return HttpResponse("This is exception page")