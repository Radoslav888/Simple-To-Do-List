from django.contrib import admin
from django.urls import path, include

from Exampleproject.tasks.views import taskboard

urlpatterns = [
    path('', taskboard, name='taskboard'),
]
