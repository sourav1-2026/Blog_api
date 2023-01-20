 # we created a api url where we want all the url should be there.

from django.contrib import admin
from django.urls import path,include




urlpatterns = [
    path('account/',include('accounts.urls')),
    path('home/',include('home.urls')),
]
