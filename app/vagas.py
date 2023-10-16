import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('recrutamento.db')
cursor = conn.cursor()

# Função para criar a tabela Vagas (caso não exista)
def criar_tabela_vagas():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Vagas (
            ID_vaga INTEGER PRIMARY KEY,
            Titulo TEXT,
            Descricao TEXT,
            Empresa TEXT,
            Salario REAL,
            Requisitos TEXT
        )
    ''')
    conn.commit()

# Função para adicionar uma vaga ao banco de dados
def adicionar_vaga(titulo, descricao, empresa, salario, requisitos):
    cursor.execute('INSERT INTO Vagas (Titulo, Descricao, Empresa, Salario, Requisitos) VALUES (?, ?, ?, ?, ?)',
                   (titulo, descricao, empresa, salario, requisitos))
    conn.commit()
    return cursor.lastrowid

# Função para criar uma vaga
def criar_vaga():
    titulo = titulo_entry.get()
    descricao = descricao_text.get("1.0", "end")
    empresa = empresa_entry.get()
    salario = salario_entry.get()
    requisitos = requisitos_text.get("1.0", "end")
    
    try:
        salario = float(salario)
    except ValueError:
        salario = 0.0

    if titulo and descricao and empresa and salario >= 0 and requisitos:
        vaga_id = adicionar_vaga(titulo, descricao, empresa, salario, requisitos)
        messagebox.showinfo("Sucesso", f"Vaga criada com sucesso (ID: {vaga_id})")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos corretamente")

# Interface de vagas
root = tk.Tk()
root.title("Recrutamento de Desenvolvedores - Vagas")

# Cria a tabela Vagas (caso não exista)
criar_tabela_vagas()

# Labels e campos de entrada
tk.Label(root, text="Título da Vaga:").pack()
titulo_entry = tk.Entry(root)
titulo_entry.pack()

tk.Label(root, text="Descrição da Vaga:").pack()
descricao_text = tk.Text(root, height=5, width=40)
descricao_text.pack()

tk.Label(root, text="Empresa:").pack()
empresa_entry = tk.Entry(root)
empresa_entry.pack()

tk.Label(root, text="Salário:").pack()
salario_entry = tk.Entry(root)
salario_entry.pack()

tk.Label(root, text="Requisitos:").pack()
requisitos_text = tk.Text(root, height=5, width=40)
requisitos_text.pack()

# Botão para criar uma vaga
criar_vaga_button = tk.Button(root, text="Criar Vaga", command=criar_vaga)
criar_vaga_button.pack()

root.mainloop()

# Fechar a conexão com o banco de dados
conn.close()
