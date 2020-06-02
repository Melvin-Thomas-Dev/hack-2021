from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from accounts.forms import RegistrationForm

def home(request):
    return render(request, 'home.html')


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration form'] = form
    else:
        form = RegistrationForm()
        context['registration form'] = form
    return render(request, 'register.html', context)
        
            
