from django.shortcuts import render
from .models import Columns, Task

def home(request):
    coluna = Columns.objects.all()

    return render(request,  'index.html', context={
        'colunas': coluna,
    })
