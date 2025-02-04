from django.shortcuts import render, get_object_or_404, redirect
from .models import Columns, Task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from .forms import TaskForms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout




def home(request):
    coluna = Columns.objects.all()

    return render(request,  'index.html', context={
        'colunas': coluna,
    })


def detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'details.html', {'task': task})

@csrf_exempt
def atualizar_tarefa(request):
    logger = logging.getLogger(__name__)
    logger.info(f"Recebido no backend: {json.loads(request.body)}")
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            logger.info(f"Dados recebidos: {dados}")

            task_id = dados.get('task_id')
            column_id = dados.get('column_id')

            if not task_id or not column_id:
                logger.error("ID da tarefa ou coluna ausente")
                return JsonResponse({'status': 'error', 'message': 'ID da tarefa ou coluna ausente'}, status=400)

            # Obter tarefa e coluna
            tarefa = Task.objects.get(id=task_id)
            coluna = Columns.objects.get(id=column_id)

            logger.info(f"Tarefa encontrada: {tarefa}")
            logger.info(f"Coluna encontrada: {coluna}")

            # Atualizar a coluna
            tarefa.columns = coluna
            tarefa.save()
            logger.info(f"Tarefa {tarefa.id} movida para a coluna {coluna.id}. Salvo no banco com sucesso.")

            return JsonResponse({'status': 'success'})
        except Task.DoesNotExist:
            logger.error("Tarefa não encontrada")
            return JsonResponse({'status': 'error', 'message': 'Tarefa não encontrada'}, status=404)
        except Columns.DoesNotExist:
            logger.error("Coluna não encontrada")
            return JsonResponse({'status': 'error', 'message': 'Coluna não encontrada'}, status=404)
        except Exception as e:
            logger.error(f"Erro inesperado: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


def criar_tarefa(request):
    if request.method == 'POST':
        form =  TaskForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForms()

    return render(request, 'criar_tarefa.html', {'form':form})

def remover_tarefa(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Tarefa Removida com Sucesso')
        
        return redirect('home')


    return render(request, 'confirm_delete.html', {'task': task})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Usuário ou Senha inválidos'})
        
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')