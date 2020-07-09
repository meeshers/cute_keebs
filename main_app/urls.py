from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('tips/', views.tips, name='tips'),
  path('discover/', views.discover, name='discover'),
  path('profile/', views.profile, name='profile'),
  path('signup/', views.signup, name='signup'),
  path('accounts/login/', views.login, name='login'),
]