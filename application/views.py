from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return render(request, 'hello.html')

def about(request):
    return HttpResponse("this is about page")