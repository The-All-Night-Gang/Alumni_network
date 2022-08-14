from django.shortcuts import render
from core.models import event
# Create your views here.
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import *
from .models import Group
from django.contrib import messages

# Create your views here.
def frontpage(request):
    return render(request, 'frontpage.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    
    else:
        form = SignUpForm

        return render(request, 'signup.html', {'form': form})

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        messages.error(request, 'Please Login into your account.')
        return redirect("login")

