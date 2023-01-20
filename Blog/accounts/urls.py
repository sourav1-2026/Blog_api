
from django.contrib import admin
from django.urls import path,include
from accounts.views import UserRegisterView,LoginView


urlpatterns = [
    path('register/',UserRegisterView.as_view()),
    path('login/',LoginView.as_view()),
]
