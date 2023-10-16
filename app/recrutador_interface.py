import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('recrutamento.db')
cursor = conn.cursor()

# Função para criar a tabela Recrutador (caso não exista)
def criar_tabela_recrutador():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Recrutador (
            ID_rec INTEGER PRIMARY KEY,
            Nome TEXT,
            Empresa TEXT,
            Contato TEXT
        )
    ''')
    conn.commit()

# Função para adicionar um recrutador ao banco de dados
def adicionar_recrutador(nome, empresa, contato):
    cursor.execute('INSERT INTO Recrutador (Nome, Empresa, Contato) VALUES (?, ?, ?)',
                   (nome, empresa, contato))
    conn.commit()
    return cursor.lastrowid

# Função para criar o perfil do recrutador
def criar_perfil_recrutador():
    nome = nome_entry.get()
    empresa = empresa_entry.get()
    contato = contato_entry.get()
    
    if nome and empresa and contato:
        recrutador_id = adicionar_recrutador(nome, empresa, contato)
        messagebox.showinfo("Sucesso", f"Perfil de Recrutador criado com sucesso (ID: {recrutador_id})")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos")

# Interface do recrutador
root = tk.Tk()
root.title("Recrutamento de Desenvolvedores - Recrutador")

# Cria a tabela Recrutador (caso não exista)
criar_tabela_recrutador()

# Labels e campos de entrada
tk.Label(root, text="Nome:").pack()
nome_entry = tk.Entry(root)
nome_entry.pack()

tk.Label(root, text="Empresa:").pack()
empresa_entry = tk.Entry(root)
empresa_entry.pack()

tk.Label(root, text="Contato:").pack()
contato_entry = tk.Entry(root)
contato_entry.pack()

# Botão para criar o perfil do recrutador
criar_perfil_button = tk.Button(root, text="Criar Perfil de Recrutador", command=criar_perfil_recrutador)
criar_perfil_button.pack()

root.mainloop()

# Fechar a conexão com o banco de dados
conn.close()
