
from django import forms

from Exampleproject.tasks.models import Task

class TaskBaseForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('publication_date', 'user', 'slug')

class TaskCreateForm(TaskBaseForm):
    class Meta:
        model = Task
        exclude = ('publication_date', 'user', 'slug', 'status')
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 10,
                },
            ),
        }

class TaskEditForm(TaskBaseForm):
    class Meta:
        model = Task
        exclude = ('publication_date', 'user', 'slug',)
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 10,
                },
            ),
        }