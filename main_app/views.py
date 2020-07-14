from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# forms
from .forms import CustomUserForm, CreateKeyboard, EditKeyboard

# models
from .models import Switch, Case, Keycap, PCB, Stabilizer, Keyboard, CustomUser

# Create your views here.
def home(request):
  error_message = ''
  form = CustomUserForm(request.POST)
  context = {'form': form, 'error_message': error_message}
  return render(request,'home.html', context)

def tips(request):
  return render(request, 'tips.html')

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
      error_message = 'Invalid signup. Please try again.'
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

### KEYBOARD CRUD ###
@login_required
def keyboard_view(request, keyboard_id):
  keyboard = Keyboard.objects.get(id=keyboard_id)
  if keyboard.user != request.user:
    return render(request, 'NA.html')
  context = {'keyboard':keyboard}
  return render(request, 'keyboard/show.html', context)

@login_required
def create_keyboard(request):
  keyboard_form = CreateKeyboard(request.POST)
  if keyboard_form.is_valid():
    keyboard = keyboard_form.save(commit=False)
    keyboard.user = request.user
    keyboard.save()
    return redirect('edit_keyboard', keyboard_id)
  context = {'keyboard_form': keyboard_form}
  return render(request,'keyboard/create.html', context)

@login_required
def keyboard_delete(request, keyboard_id):
  keyboard = Keyboard.objects.get(id=keyboard_id)
  keyboard.delete()
  return redirect('profile')

@login_required
def keyboard_edit(request, keyboard_id):
  keyboard = Keyboard.objects.get(id=keyboard_id)
  if request.method == 'POST':
    edit_keyboard = EditKeyboard(request.POST, instance=keyboard)
    if edit_keyboard.is_valid():
      edit_keyboard.save()
      return redirect('show', keyboard_id=keyboard_id)
  else:
    edit_keyboard = EditKeyboard(instance=keyboard)
  context={'keyboard':keyboard, 'edit_keyboard': edit_keyboard}
  return render(request, 'keyboard/edit.html',context)

### PARTS PAGES ROUTES ###
@login_required
def discover(request):
  switches = Switch.objects.all()
  cases = Case.objects.all()
  keycaps = Keycap.objects.all()
  pcbs = PCB.objects.all()
  stabilizers = Stabilizer.objects.all()
  context = {'switches':switches, 'cases': cases,'keycaps': keycaps,'pcbs': pcbs,'stabilizers': stabilizers}
  return render(request, 'discover.html', context)

@login_required
def cases(request):
  cases = Case.objects.all()
  context = {'cases':cases }
  return render(request, 'part/cases.html', context)

@login_required
def switches(request):
  switches = Switch.objects.all()
  context = {'switches':switches }
  return render(request, 'part/switches.html', context)

@login_required
def keycaps(request):
  keycaps = Keycap.objects.all()
  context = {'keycaps':keycaps }
  return render(request, 'part/keycaps.html', context)

@login_required
def stabilizers(request):
  stabilizers = Stabilizer.objects.all()
  context = {'stabilizers':stabilizers }
  return render(request, 'part/stabilizers.html', context)

@login_required
def pcbs(request):
  pcbs = PCB.objects.all()
  context = {'pcbs':pcbs }
  return render(request, 'part/pcbs.html', context)

### PARTS SHOW PAGES ROUTES ###
@login_required
def case(request, case_id):
  case = Case.objects.get(id=case_id)
  context = {'case':case}
  return render(request, 'part/show/case.html', context)

@login_required
def switch(request, switch_id):
  switch = Switch.objects.get(id=switch_id)
  context = {'switch':switch}
  return render(request, 'part/show/switch.html', context)

@login_required
def keycap(request, keycap_id):
  keycap = Keycap.objects.get(id=keycap_id)
  context = {'keycap':keycap}
  return render(request, 'part/show/keycap.html', context)

@login_required
def stabilizer(request, stabilizer_id):
  stabilizer = Stabilizer.objects.get(id=stabilizer_id)
  context = {'stabilizer':stabilizer}
  return render(request, 'part/show/stabilizer.html', context)

@login_required
def pcb(request, pcb_id):
  pcb = PCB.objects.get(id=pcb_id)
  context = {'pcb':pcb}
  return render(request, 'part/show/pcb.html', context)