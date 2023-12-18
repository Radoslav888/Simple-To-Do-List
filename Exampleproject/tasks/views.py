from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from Exampleproject.tasks.forms import TaskCreateForm, TaskEditForm
from django.views import generic as views

from Exampleproject.tasks.models import Task

UserModel = get_user_model()
# Create your views here!


def taskboard(request, pk):
    user = UserModel.objects.filter(pk=pk).get()
    tasks = user.task_set.all().order_by("status")
    page = request.GET.get('page', 1)
    paginator = Paginator(tasks, 9)

    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)

    context = {
        'tasks': tasks,
        'object': user,
    }
    return render(request, 'tasks/taskboard.html', context)

def add_task(request):
    if request.method == 'POST':
        TaskForm = TaskCreateForm(request.POST)

        if TaskForm.is_valid():
            task_form = TaskForm.save(commit=False)
            task_form.user = request.user
            task_form.status = False
            task_form.save()

            return redirect('taskboard', pk=request.user.id)
        else:
            print(TaskForm.errors)
    else:
        TaskForm = TaskCreateForm()
    context = {
        'task_form': TaskForm,
    }
    return render(request, 'tasks/add-task.html', context)



def edit_task(request, slug):
    task = Task.objects.filter(slug=slug).get()
    if request.method == 'POST':
        TaskForm = TaskEditForm(request.POST, instance=task)

        if TaskForm.is_valid():
            task_form = TaskForm.save(commit=False)
            task_form.user = request.user
            
            task_form.save()

            return redirect('taskboard', pk=request.user.id)
        else:
            print(TaskForm.errors)
    else:
        TaskForm = TaskEditForm(instance=task)
    context = {
        'task_form': TaskForm,
        'task': task,
    }
    return render(request, 'tasks/edit-task.html', context)


class DeleteTaskView(views.DeleteView):
    template_name = 'tasks/task-delete.html'
    model = Task
    def get_success_url(self, **kwargs):
        return reverse_lazy('taskboard', kwargs={
            'pk': self.request.user.id,
        })