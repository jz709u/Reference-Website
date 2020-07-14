from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('index')

def test(request):
    return HttpResponse('test')

def test2(request):
    return HttpResponse('test2')

def test3(request):
    return HttpResponse('test3')
