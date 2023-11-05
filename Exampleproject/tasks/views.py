from django.shortcuts import render

# Create your views here.


def taskboard(request):
    return render(request, 'tasks/taskboard.html')
