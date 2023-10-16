import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3
import os

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('recrutamento.db')
cursor = conn.cursor()

# Função para criar a tabela Candidato (caso não exista)
def criar_tabela_candidato():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Candidato (
            ID_cand INTEGER PRIMARY KEY,
            Nome TEXT,
            E_mail TEXT,
            Experiencia TEXT,
            Curriculo BLOB
        )
    ''')
    conn.commit()

# Função para adicionar um candidato ao banco de dados
def adicionar_candidato(nome, email, experiencia, curriculo):
    cursor.execute('INSERT INTO Candidato (Nome, E_mail, Experiencia, Curriculo) VALUES (?, ?, ?, ?)',
                   (nome, email, experiencia, curriculo))
    conn.commit()
    return cursor.lastrowid

# Função para fazer upload de um currículo em PDF
def fazer_upload_curriculo():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        with open(file_path, 'rb') as file:
            return file.read()
    return None

# Função para criar o perfil do candidato
def criar_perfil_candidato():
    nome = nome_entry.get()
    email = email_entry.get()
    experiencia = experiencia_text.get("1.0", "end")
    curriculo = fazer_upload_curriculo()
    
    if nome and email and experiencia and curriculo:
        candidato_id = adicionar_candidato(nome, email, experiencia, curriculo)
        messagebox.showinfo("Sucesso", f"Perfil criado com sucesso (ID: {candidato_id})")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos e faça upload do currículo em PDF")

# Interface do candidato
root = tk.Tk()
root.title("DEVConnect - Candidato")

# Cria a tabela Candidato (caso não exista)
criar_tabela_candidato()

# Labels e campos de entrada
tk.Label(root, text="Nome:").pack()
nome_entry = tk.Entry(root)
nome_entry.pack()

tk.Label(root, text="E-mail:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Experiência:").pack()
experiencia_text = tk.Text(root, height=5, width=40)
experiencia_text.pack()

# Botão para fazer upload de currículo
upload_button = tk.Button(root, text="Fazer Upload de Currículo (PDF)", command=fazer_upload_curriculo)
upload_button.pack()

# Botão para criar o perfil do candidato
criar_perfil_button = tk.Button(root, text="Criar Perfil de Candidato", command=criar_perfil_candidato)
criar_perfil_button.pack()

root.mainloop()

# Fechar a conexão com o banco de dados
conn.close()
