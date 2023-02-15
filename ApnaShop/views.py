from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("About Page")

def contact(request):
    return HttpResponse("Contact Page")    

def tracker(request):
    return HttpResponse("Tracking Page")

def search(request):
    return HttpResponse("Search Page")

def productView(request):
    return HttpResponse("ProductView Page")

def checkout(request):
    return HttpResponse("Checkout Page");