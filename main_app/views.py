from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# forms
from .forms import CustomUserForm, CreateKeyboard

# models
from .models import Switch, Case, Keycap, PCB, Stabilizer, Keyboard, CustomUser

# Create your views here.
def home(request):
  form = CustomUserForm(request.POST)
  context = {'form': form}
  return render(request,'home.html', context)

def tips(request):
  return render(request, 'tips.html')

def discover(request):
  return render(request, 'discover.html')

#sign up/register
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = CustomUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('profile')
    else:
      error_message = 'Invalid signup please try again'
  else:
    form = CustomUserForm()
  context = {'form': form, 'error_message': error_message}
  return render(request,'home.html',context)

@login_required
def profile(request):
  return render(request, 'profile.html')