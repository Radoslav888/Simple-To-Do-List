from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from Exampleproject.tasks.models import Task

UserModel = get_user_model()
# Create your views here!


def taskboard(request, pk):
    user = UserModel.objects.filter(pk=pk).get()
    tasks = user.task_set.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(tasks, 3)

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