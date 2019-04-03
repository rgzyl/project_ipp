from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForms

def registration(request):
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Twoje konto zostało utworzone! Możesz się zalogować.')
            return redirect('login')
    else:
        form = RegistrationForms()
    return render(request, 'users/registration.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
