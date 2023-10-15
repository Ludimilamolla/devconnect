import tkinter as tk
import sqlite3
from tkinter import messagebox

# Função para criar o banco de dados e a tabela
def criar_banco_dados():
    conn = sqlite3.connect('recrutamento.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS desenvolvedores (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            sobrenome TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Função para cadastrar um desenvolvedor
def cadastrar_desenvolvedor():
    nome = nome_entry.get()
    sobrenome = sobrenome_entry.get()
    email = email_entry.get()
    
    conn = sqlite3.connect('recrutamento.db')
    c = conn.cursor()
    c.execute("INSERT INTO desenvolvedores (nome, sobrenome, email) VALUES (?, ?, ?)", (nome, sobrenome, email))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Sucesso", "Desenvolvedor cadastrado com sucesso!")

# Função para listar desenvolvedores
def listar_desenvolvedores():
    conn = sqlite3.connect('recrutamento.db')
    c = conn.cursor()
    c.execute("SELECT * FROM desenvolvedores")
    desenvolvedores = c.fetchall()
    conn.close()
    
    lista_desenvolvedores.delete(0, tk.END)
    
    for desenvolvedor in desenvolvedores:
        lista_desenvolvedores.insert(tk.END, f"{desenvolvedor[1]} {desenvolvedor[2]} - {desenvolvedor[3]}")

# Criar a janela principal
root = tk.Tk()
root.title("Recrutamento de Desenvolvedores")

# Criar e posicionar os elementos na janela
tk.Label(root, text="Nome:").grid(row=0, column=0)
nome_entry = tk.Entry(root)
nome_entry.grid(row=0, column=1)

tk.Label(root, text="Sobrenome:").grid(row=1, column=0)
sobrenome_entry = tk.Entry(root)
sobrenome_entry.grid(row=1, column=1)

tk.Label(root, text="E-mail:").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

cadastrar_button = tk.Button(root, text="Cadastrar Desenvolvedor", command=cadastrar_desenvolvedor)
cadastrar_button.grid(row=3, columnspan=2)

listar_button = tk.Button(root, text="Listar Desenvolvedores", command=listar_desenvolvedores)
listar_button.grid(row=4, columnspan=2)

lista_desenvolvedores = tk.Listbox(root, width=40)
lista_desenvolvedores.grid(row=5, columnspan=2)

# Inicializar o banco de dados
criar_banco_dados()

# Iniciar o loop principal da aplicação
root.mainloop()
