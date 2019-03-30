from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Test</h1>')

def about(request):
    return HttpResponse('<h1>Test 1</h1>')
