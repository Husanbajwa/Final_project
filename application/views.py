from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')
def about(request):
    return render('about.html')
def contact(request):
    return render('contact.html')