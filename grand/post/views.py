from django.shortcuts import render
from .models import Mem

def home(request):
    context = {
        'posts': Mem.objects.all()
    }
    return render(request, 'post/home.html', context)

def about(request):
    return render(request, 'post/about.html', {'title':'About'})
