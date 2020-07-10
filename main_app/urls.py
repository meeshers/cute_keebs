from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('tips/', views.tips, name='tips'),
  path('discover/', views.discover, name='discover'),
  path('profile/', views.profile, name='profile'),
  path('signup/', views.signup, name='signup'),
  path('keyboard/<int:keyboard_id>', views.keyboard_view, name="show"),
  path('create-keyboard', views.create_keyboard, name='create_keyboard'),
  path('delete_keyboard/<int:keyboard_id>', views.keyboard_delete, name='keyboard_delete'),
]