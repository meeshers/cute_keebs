from django import forms
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Switch, Case, Keycap, PCB, Stabilizer, Keyboard, CustomUser

class CustomUserForm(UserCreationForm):
  class Meta:
    model = CustomUser
    fields = ['username', 'full_name','email']

class CreateKeyboard(forms.ModelForm):
  class Meta:
    model = Keyboard
    fields = ['name','status', 'case', 'switch', 'pcb', 'stabilizer', 'keycap', 'description']

class EditKeyboard(forms.ModelForm):
  class Meta:
    model = Keyboard
    fields = ['name','status', 'case', 'switch', 'pcb', 'stabilizer', 'keycap', 'description']

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