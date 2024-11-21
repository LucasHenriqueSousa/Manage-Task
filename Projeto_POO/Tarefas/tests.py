from django.test import TestCase
from .crud_tarefa import create_table_tarefa, create_tarefa, read_tarefa, update_tarefa, delete_tarefa

class TarefaTests(TestCase):
    """Testes para verificar as operações CRUD na tabela de tarefas."""

    def setUp(self):
        """Configuração inicial antes de cada teste."""
        # Cria a tabela de tarefas e adiciona uma tarefa de teste
        create_table_tarefa()
        create_tarefa("Tarefa Teste", False)  # Tarefa inicial para testes

    def test_create_tarefa(self):
        """
        Teste de criação de tarefa.
        Verifica se uma nova tarefa é corretamente inserida na tabela.
        """
        create_tarefa("Nova Tarefa", True)  # Cria uma nova tarefa com o status de "feita"
        tarefas = read_tarefa()
        # Verifica se a tarefa foi adicionada com o nome "Nova Tarefa"
        self.assertTrue(any(tarefa[1] == "Nova Tarefa" for tarefa in tarefas))

    def test_read_tarefa(self):
        """
        Teste de leitura de tarefas.
        Verifica se a leitura das tarefas retorna a lista correta.
        """
        tarefas = read_tarefa()
        # Deve haver pelo menos uma tarefa, a tarefa inicial de "Tarefa Teste"
        self.assertGreaterEqual(len(tarefas), 1)
        # Verifica se a tarefa inicial existe e possui o status correto
        self.assertTrue(any(tarefa[1] == "Tarefa Teste" and tarefa[2] == 0 for tarefa in tarefas))

    def test_update_tarefa(self):
        """
        Teste de atualização de tarefa.
        Verifica se a atualização de uma tarefa específica altera seu status e nome corretamente.
        """
        tarefas = read_tarefa()
        tarefa_id = tarefas[0][0]  # Seleciona o ID da primeira tarefa
        update_tarefa(tarefa_id, "Tarefa Atualizada", True)  # Atualiza a tarefa
        tarefa_atualizada = read_tarefa()
        # Verifica se a tarefa foi atualizada com o nome "Tarefa Atualizada" e status "feita"
        self.assertTrue(any(tarefa[0] == tarefa_id and tarefa[1] == "Tarefa Atualizada" and tarefa[2] == 1 
                            for tarefa in tarefa_atualizada))

    def test_delete_tarefa(self):
        """
        Teste de exclusão de tarefa.
        Verifica se uma tarefa é corretamente removida da tabela.
        """
        tarefas = read_tarefa()
        tarefa_id = tarefas[0][0]  # Seleciona o ID da primeira tarefa para exclusão
        delete_tarefa(tarefa_id)  # Exclui a tarefa
        tarefas_apos_delete = read_tarefa()
        # Verifica que a tarefa não existe mais na tabela
        self.assertFalse(any(tarefa[0] == tarefa_id for tarefa in tarefas_apos_delete))
