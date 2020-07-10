from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('tips/', views.tips, name='tips'),
  path('profile/', views.profile, name='profile'),
  path('signup/', views.signup, name='signup'),

  # keyboard crud routes
  path('keyboard/<int:keyboard_id>', views.keyboard_view, name="show"),
  path('create-keyboard', views.create_keyboard, name='create_keyboard'),
  path('delete-keyboard/<int:keyboard_id>', views.keyboard_delete, name='keyboard_delete'),
  path('edit-keyboard/<int:keyboard_id>', views.keyboard_edit, name="edit_keyboard"),

  # keyboard parts routes
  path('discover/', views.discover, name='discover'),
  path('discover/cases', views.cases, name="cases"),
  path('discover/switches', views.switches, name="switches"),
  path('discover/keycaps', views.keycaps, name="keycaps"),
  path('discover/stabilizers', views.stabilizers, name="stabilizers"),
  path('discover/pcbs', views.pcbs, name="pcbs"),

  # keyboard show part routes
  path('discover/cases/<int:case_id>', views.case, name="case"),
  path('discover/switches/<int:switch_id>', views.switch, name="switch"),
  path('discover/keycaps/<int:keycap_id>', views.keycap, name="keycap"),
  path('discover/stabilizers/<int:stabilizer_id>', views.stabilizer, name="stabilizer"),
  path('discover/pcbs/<int:pcb_id>', views.pcb, name="pcb"),
]