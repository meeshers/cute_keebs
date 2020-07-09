from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# forms

# models
from .models import Switch, Case, Keycap, PCB, Stabilizer, Keyboard, CustomUser

# Create your views here.
def home(request):
  return render(request,'home.html')

def tips(request):
  return HttpResponse('<h1>This is the tips page</h1>')

def discover(request):
  return HttpResponse('<h1>This is the parts page</h1>')