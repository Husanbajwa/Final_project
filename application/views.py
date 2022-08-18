from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpRequest

def sayhello(request):
    return HTTPResponse('Hello World')