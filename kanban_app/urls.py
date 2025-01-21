from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/<int:task_id>/', views.detail, name='detail'),
    path('atualizar-tarefa/', views.atualizar_tarefa, name='atualizar_tarefa' ),
]
