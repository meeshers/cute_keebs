from django.contrib import admin

# Register your models here.
from .models import Switch, Case, Keycap, PCB, Stabilizer, Keyboard, CustomUser, Tracker

admin.site.register(Switch)
admin.site.register(Case)
admin.site.register(Keycap)
admin.site.register(PCB)
admin.site.register(Stabilizer)
admin.site.register(Keyboard)
admin.site.register(CustomUser)
admin.site.register(Tracker)