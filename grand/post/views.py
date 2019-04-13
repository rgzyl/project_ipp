from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Mem

def home(request):
    context = {
        'posts': Mem.objects.all()
    }
    return render(request, 'post/home.html', context)

class MemListView(ListView):
    model = Mem
    template_name = 'post/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class MemDetailView(DetailView):
    model = Mem

class MemCreateView(LoginRequiredMixin, CreateView):
    model = Mem
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class MemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Mem
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        mem = self.get_object()
        if self.request.user == mem.author:
            return True
        return False
    
class MemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mem
    success_url = '/'

    def test_func(self):
        mem = self.get_object()
        if self.request.user == mem.author:
            return True
        return False

def about(request):
    return render(request, 'post/about.html', {'title':'About'})

def contact(request):
    return render(request, 'post/contact.html', {'title':'Contact'})
