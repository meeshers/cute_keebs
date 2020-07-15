from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# forms
from .forms import CustomUserForm, CreateKeyboard, EditKeyboard, CreateCase, CreateKeycap, CreatePCB, CreateStabilizer, CreateSwitch, CreateTracker

# models
from .models import Switch, Case, Keycap, PCB, Stabilizer, Keyboard, CustomUser, Tracker

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
    tracker_form = CreateTracker(request.POST)
    if keyboard_form.is_valid():
      keyboard = keyboard_form.save(commit=False)
      keyboard.user = request.user
      keyboard.save()
    elif tracker_form.is_valid():
      tracker = tracker_form.save(commit=False)
      tracker.user = request.user
      tracker.save()
    return redirect('profile')
  else:
      keyboards = Keyboard.objects.all().filter(user=request.user.id)
      trackers = Tracker.objects.all().filter(user=request.user.id)
  context = {"keyboards":keyboards,"trackers":trackers}
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
  case_form = CreateCase(request.POST)
  context = {'cases':cases, 'case_form': case_form }
  return render(request, 'part/cases.html', context)

@login_required
def switches(request):
  switches = Switch.objects.all()
  switch_form = CreateSwitch(request.POST)
  context = {'switches':switches, 'switch_form':switch_form }
  return render(request, 'part/switches.html', context)

@login_required
def keycaps(request):
  keycaps = Keycap.objects.all()
  keycap_form = CreateKeycap(request.POST)
  context = {'keycaps':keycaps, 'keycap_form':keycap_form }
  return render(request, 'part/keycaps.html', context)

@login_required
def stabilizers(request):
  stabilizers = Stabilizer.objects.all()
  stab_form = CreateStabilizer(request.POST)
  context = {'stabilizers':stabilizers, 'stab_form':stab_form }
  return render(request, 'part/stabilizers.html', context)

@login_required
def pcbs(request):
  pcbs = PCB.objects.all()
  pcb_form = CreatePCB(request.POST)
  context = {'pcbs':pcbs, 'pcb_form': pcb_form }
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

### PART CREATION ###
@login_required
def create_case(request):
  case_form = CreateCase(request.POST)
  if case_form.is_valid():
    case = case_form.save()
    return redirect('cases')
  context = {'case_form': case_form}
  return render(request, 'cases', context)

@login_required
def create_switch(request):
  switch_form = CreateSwitch(request.POST)
  if switch_form.is_valid():
    switch = switch_form.save()
    return redirect('switches')
  context = {'switch_form': switch_form}
  return render(request, 'switches', context)

@login_required
def create_keycap(request):
  keycap_form = CreateKeycap(request.POST)
  if keycap_form.is_valid():
    keycap = keycap_form.save()
    return redirect('keycaps')
  context = {'keycap_form': keycap_form}
  return render(request, 'keycaps', context)

@login_required
def create_pcb(request):
  pcb_form = CreatePCB(request.POST)
  if pcb_form.is_valid():
    pcb = pcb_form.save()
    return redirect('pcbs')
  context = {'pcb_form': pcb_form}
  return render(request, 'pcbs', context)

@login_required
def create_stab(request):
  stab_form = CreateStabilizer(request.POST)
  if stab_form.is_valid():
    stab = stab_form.save()
    return redirect('stabs')
  context = {'stab_form': stab_form}
  return render(request, 'stabs', context)

### IC/GB TRACKER ROUTES ###
def create_tracker(request):
  tracker_form = CreateTracker(request.POST)
  if tracker_form.is_valid():
    tracker = tracker_form.save(commit=False)
    tracker.user = request.user
    tracker.save()
    return redirect('profile')
  context = {'tracker_form': tracker_form}
  return render(request, 'tracker/create.html', context)