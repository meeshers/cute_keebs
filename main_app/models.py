from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
  full_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=50)

  USERNAME_FIELD = "username"

  def __str__(self):
    return self.username

# tactile/linear/clicky/misc
SWITCH_TYPE = (
  ('LI', 'Linear'),
  ('TA', 'Tactile'),
  ('CL', 'Clicky'),
  ('MI', 'Other')
)

class Switch(models.Model):
  name = models.CharField(max_length=50)
  switch_type = models.CharField(max_length=2, choices=SWITCH_TYPE, default=SWITCH_TYPE[0][0]) 
  description = models.TextField(max_length=1000)
  image = models.CharField(max_length=1000)

  def __str__(self):
    return self.name

# case form factors
FORM_TYPE = (
  ('40', '40%'),
  ('60', '60%'),
  ('65', '65%'),
  ('75', '75% (TKL)'),
  ('10', '100% (Full size)'),
  ('OR', 'Ortholinear'),
  ('ER', 'Ergonomic')
)

class Case(models.Model):
  name = models.CharField(max_length=50)
  form_type = models.CharField(max_length=2, choices=FORM_TYPE, default=FORM_TYPE[0][0])
  material = models.CharField(max_length=100)
  description = models.TextField(max_length=1000)
  image = models.CharField(max_length=1000)

  def __str__(self):
    return self.name

# keycap profiles
KEY_PROFILE = (
  ('DS', 'DSA profile'),
  ('SA', 'SA profile'),
  ('OE', 'OEM profile'),
  ('KT', 'KAT profile'),
  ('CH', 'Cherry profile')
)

KEY_MATERIAL = (
  ('ABS', 'ABS'),
  ('PBT', 'PBT'),
  ('POM', 'POM'),
)

class Keycap(models.Model):
  name = models.CharField(max_length=50)
  material = models.CharField(max_length=3, choices=KEY_MATERIAL, default=KEY_MATERIAL[0][0])
  profile = models.CharField(max_length=2, choices=KEY_PROFILE, default=KEY_PROFILE[0][0])
  description = models.TextField(max_length=1000)
  image = models.CharField(max_length=1000)

  def __str__(self):
    return self.name

# pcb types
PCB_TYPE = (
  ('SL', 'Solder'),
  ('HS', 'Hotswap')
)

class PCB(models.Model):
  name = models.CharField(max_length=50)
  pcb_type = models.CharField(max_length=2, choices=PCB_TYPE, default=PCB_TYPE[0][0]) 
  description = models.TextField(max_length=1000)
  image = models.CharField(max_length=1000)

  def __str__(self):
    return self.name

# stabilizer types
STAB = (
  ('S', 'Screw-in Stabilizers'),
  ('P', 'PCB-Mounted')
)

class Stabilizer(models.Model):
  name = models.CharField(max_length=50)
  stab_type = models.CharField(max_length=1, choices=STAB, default=STAB[0][0])
  description = models.TextField(max_length=1000)
  image = models.CharField(max_length=1000)

  def __str__(self):
    return self.name

class Keyboard(models.Model):
  name = models.CharField(max_length=50)
  case = models.OneToOneField(Case, on_delete=models.CASCADE)
  switch = models.OneToOneField(Switch, on_delete=models.CASCADE)
  pcb = models.OneToOneField(PCB, on_delete=models.CASCADE)
  stabilizer = models.OneToOneField(Stabilizer, on_delete=models.CASCADE)
  keycap = models.OneToOneField(Keycap, on_delete=models.CASCADE)
  user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
  description = models.TextField(max_length=1000)

  def __str__(self):
    return self.name
