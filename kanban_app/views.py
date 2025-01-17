from django.shortcuts import render, get_object_or_404
from .models import Columns, Task

def home(request):
    coluna = Columns.objects.all()

    return render(request,  'index.html', context={
        'colunas': coluna,
    })


def detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'details.html', {'task': task})
