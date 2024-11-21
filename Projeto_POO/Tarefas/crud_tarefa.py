import sqlite3
from django.utils import timezone

def connect():
    """
    Conecta ao banco de dados SQLite.
    :return: Conexão com o banco de dados.
    """
    return sqlite3.connect("Managetask.db")

def create_table_tarefa():
    """
    Cria a tabela de tarefas no banco de dados, se ela não existir.
    """
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefa(
            id_tarefa INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_tarefa VARCHAR(50) NOT NULL,
            feita BOOLEAN NOT NULL,
            data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        conn.commit()

def create_tarefa(nome_tarefa, feita):
    """
    Insere uma nova tarefa na tabela de tarefas.
    :param nome_tarefa: Nome da tarefa.
    :param feita: Status da tarefa (True para feita, False para não feita).
    """
    data_criacao = timezone.localtime(timezone.now())
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO tarefa (nome_tarefa, feita, data_criacao) VALUES (?,?,?)
        ''', (nome_tarefa, feita, data_criacao))
        conn.commit()

def read_tarefa():
    """
    Lê todas as tarefas da tabela de tarefas.
    :return: Lista de tarefas (id_tarefa, nome_tarefa, feita, data_criacao).
    """
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarefa")
        tarefas = cursor.fetchall()
        print(tarefas)  # Adicione esta linha para verificar o conteúdo
        return tarefas

def update_tarefa(id_tarefa, nome_tarefa, feita):
    """
    Atualiza uma tarefa existente na tabela de tarefas.
    :param id_tarefa: ID da tarefa a ser atualizada.
    :param nome_tarefa: Novo nome da tarefa.
    :param feita: Novo status da tarefa (True para feita, False para não feita).
    """
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE tarefa SET nome_tarefa = ?, feita = ? WHERE id_tarefa = ?
        ''', (nome_tarefa, feita, id_tarefa))
        conn.commit()

def delete_tarefa(id_tarefa):
    """
    Exclui uma tarefa da tabela de tarefas.
    :param id_tarefa: ID da tarefa a ser excluída.
    """
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tarefa WHERE id_tarefa = ?", (id_tarefa,))
        conn.commit()
