from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse("app1 first function")
def second(request):
    return HttpResponse("app1 second function")