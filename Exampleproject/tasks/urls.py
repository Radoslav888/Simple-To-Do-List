from django.contrib import admin
from django.urls import path, include

from Exampleproject.tasks.views import DeleteTaskView, edit_task, taskboard, add_task

urlpatterns = [
    path('<int:pk>/', taskboard, name='taskboard'),
    path('add/', add_task, name='add task'),
    path('edit/<str:slug>', edit_task, name='edit task'),
    path('delete/<str:slug>', DeleteTaskView.as_view(), name='delete task'),
]
