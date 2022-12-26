from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def four(request):
    return HttpResponse("app2 first function")
def five(request):
    return HttpResponse("app2 second function")