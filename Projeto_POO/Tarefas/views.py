from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .crud_tarefa import create_tarefa, read_tarefa, update_tarefa, delete_tarefa

def listar_tarefas(request):
    # Obter o valor do filtro de status do GET
    status = request.GET.get('status')
    
    # Ler as tarefas do banco de dados
    tarefas = read_tarefa()
    print(tarefas)  # Verifique os dados retornados
    
    # Aplicar o filtro, se fornecido
    if status == "1":  # Filtrar por tarefas feitas
        tarefas = [tarefa for tarefa in tarefas if tarefa[2] == 1]
    elif status == "0":  # Filtrar por tarefas não feitas
        tarefas = [tarefa for tarefa in tarefas if tarefa[2] == 0]
    
    # Renderizar o template com as tarefas (filtradas ou não)
    return render(request, 'listar_tarefas.html', {'tarefas': tarefas})


def criar_tarefa(request):
    if request.method == 'POST':
        nome_tarefa = request.POST.get('nome_tarefa')
        # Aqui, pegue o valor enviado e converta diretamente para 1 ou 0
        feita = request.POST.get('feita', None)
        if feita is not None:
            feita = int(feita)  # Converte para 1 ou 0 dependendo do valor
        create_tarefa(nome_tarefa, feita)
        return redirect('listar_tarefas')
    return render(request, 'criar_tarefa.html')


def atualizar_tarefa(request, id_tarefa):
    if request.method == 'POST':
        nome_tarefa = request.POST.get('nome_tarefa')
        # Verifique se o status da tarefa é '1' ou '0'
        feita = request.POST.get('feita', None)
        if feita is not None:
            feita = int(feita)  # Convertendo o valor para 1 ou 0
        update_tarefa(id_tarefa, nome_tarefa, feita)
        return redirect('listar_tarefas')

    # Obtém a tarefa específica pelo ID e todas as tarefas existentes
    tarefa = next((t for t in read_tarefa() if t[0] == id_tarefa), None)
    tarefas_existentes = read_tarefa()  # Todas as tarefas para exibir na página

    return render(request, 'atualizar_tarefa.html', {
        'tarefa': tarefa,
        'tarefas_existentes': tarefas_existentes
    })



def deletar_tarefa(request, id_tarefa):
    delete_tarefa(id_tarefa)
    return redirect('listar_tarefas')

def visualizar_status_tarefas(request):
    # Ler as tarefas do banco de dados
    tarefas = read_tarefa()

    # Criar uma lista de tarefas com o status 'feita' ou 'não feita'
    tarefas_status = [
        {"id": tarefa[0], "nome": tarefa[1], "status": "Feita" if tarefa[2] == 1 else "Não Feita"}
        for tarefa in tarefas
    ]
    
    # Renderizar o template com as tarefas e seus status
    return render(request, 'visualizar_status_tarefas.html', {'tarefas_status': tarefas_status})
