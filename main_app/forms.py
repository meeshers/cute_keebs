from django import forms
from django.forms import ModelForm, Select
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Switch, Case, Keycap, PCB, Stabilizer, Keyboard, CustomUser, Tracker

class CustomUserForm(UserCreationForm):
  class Meta:
    model = CustomUser
    fields = ['username', 'full_name','email']

class CreateKeyboard(forms.ModelForm):
  class Meta:
    model = Keyboard
    fields = ['name','status', 'description']

class EditKeyboard(forms.ModelForm):
  class Meta:
    model = Keyboard
    fields = ['name','status', 'case', 'switch', 'pcb', 'stabilizer', 'keycap', 'description']
"""     widgets = {
      'case': Select(),
      'switch': Select(),
      'pcb': Select(),
      'stabilizer': Select(),
      'keycap': Select()
    } """

# forms for stretch goal
class CreateSwitch(forms.ModelForm):
  class Meta:
    model = Switch
    fields = ['name', 'switch_type', 'image', 'description']

class CreateCase(forms.ModelForm):
  class Meta:
    model = Case
    fields = ['name', 'form_type', 'material', 'image', 'description']

class CreateKeycap(forms.ModelForm):
  class Meta:
    model = Keycap
    fields = ['name', 'material', 'profile', 'image', 'description']

class CreatePCB(forms.ModelForm):
  class Meta:
    model = PCB
    fields = ['name', 'pcb_type', 'image', 'description']

class CreateStabilizer(forms.ModelForm):
  class Meta:
    model = Stabilizer
    fields = ['name', 'stab_type', 'image', 'description']

# IC/GB Tracker form
class DateInput(forms.DateInput):
  input_type='date'

class CreateTracker(forms.ModelForm):
  class Meta:
    model = Tracker
    widgets ={
      'date': DateInput()
    }
    fields = ['title', 'interest_type', 'date', 'description']

class EditTracker(forms.ModelForm):
  class Meta:
    model = Tracker
    widgets ={
      'date': DateInput()
    }
    fields = ['title', 'interest_type', 'date', 'description']