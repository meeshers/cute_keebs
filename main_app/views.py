from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
  return HttpResponse('<h1>This is the home page</h1>')

def tips(request):
  return HttpResponse('<h1>This is the tips page</h1>')

def discover(request):
  return HttpResponse('<h1>This is the parts page</h1>')