from django.urls import path
from HomePage.views import *
from . import views
from django.urls import include, re_path

urlpatterns = [
    re_path('SignUp/', views.RegisterView, name='SignUp'),
    re_path('SignIn/', views.LoginView, name='SignIn'),
    re_path('SignOut/', views.logout_View, name= 'SignOut')
]