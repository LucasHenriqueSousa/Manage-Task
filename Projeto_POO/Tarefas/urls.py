from django.urls import path
from django.http import HttpResponse
from .views import listar_tarefas, criar_tarefa, atualizar_tarefa, deletar_tarefa, visualizar_status_tarefas

urlpatterns = [
    path('visualizar/', listar_tarefas, name='listar_tarefas'),
    path('criar/', criar_tarefa, name='criar_tarefa'),
    path('atualizar/<int:id_tarefa>/', atualizar_tarefa, name='atualizar_tarefa'),
    path('deletar/<int:id_tarefa>/', deletar_tarefa, name='deletar_tarefa'),
    path('status/', visualizar_status_tarefas, name='visualizar_status_tarefas')
]
