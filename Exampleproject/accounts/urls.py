from django.contrib import admin
from django.urls import path, include

from Exampleproject.accounts.views import SignUpView, SingInView, SignOutView
from Exampleproject.common.views import index

urlpatterns = [
    path('register', SignUpView.as_view(), name='register'),
    path('login', SingInView.as_view(), name='log in'),
    path('logout', SignOutView.as_view(), name='log out'),
]