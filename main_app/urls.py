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
]