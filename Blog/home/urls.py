
from django.contrib import admin
from django.urls import path,include
from home.views import BlogView


urlpatterns = [
    path('blog/',BlogView.as_view()),
]
