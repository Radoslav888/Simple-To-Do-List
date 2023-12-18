from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from Exampleproject.tasks.models import Task




# Register your models here.


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ('name', 'description', 'status', )
    list_filter = ('user',)


