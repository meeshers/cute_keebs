from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
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
  if request.method == 'POST':
    keyboard_form = CreateKeyboard(request.POST)
    if keyboard_form.is_valid():
      keyboard = keyboard_form.save(commit=False)
      keyboard.user = request.user
      keyboard.save()
    return redirect('profile')
  else:
      keyboards = Keyboard.objects.all().filter(user=request.user.id)
  context = {"keyboards":keyboards}
  return render(request, 'profile.html',context)

@login_required
def keyboard_view(request, keyboard_id):
  keyboard = Keyboard.objects.get(id=keyboard_id)
  context = {'keyboard':keyboard}
  return render(request, 'keyboard/show.html', context)

@login_required
def create_keyboard(request):
  keyboard_form = CreateKeyboard(request.POST)
  if keyboard_form.is_valid():
    keyboard = keyboard_form.save(commit=False)
    keyboard.user = request.user
    keyboard.save()
  context = {'keyboard_form': keyboard_form}
  return render(request,'keyboard/create.html', context)

@login_required
def keyboard_delete(request, keyboard_id):
  keyboard = Keyboard.objects.get(id=keyboard_id)
  keyboard.delete()
  return redirect('profile')
