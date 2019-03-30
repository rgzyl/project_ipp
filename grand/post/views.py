from django.shortcuts import render

posts = [
    {
        'author': 'Radek',
        'title': 'Post nr 1',
        'content': 'Ciekawe co to bedzie',
        'date_posted': '27 maja 2019'
    },
    {
        'author': 'Johann',
        'title': 'Post nr 2',
        'content': 'Ciekawe co to bedzie',
        'date_posted': '21 maja 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'post/home.html')

def about(request):
    return render(request, 'post/about.html')
