import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3
import os
import re

# Funçao - Conectar ao banco de dados SQLite
conn = sqlite3.connect('recrutamento.db')
cursor = conn.cursor()

# Funçao - Criar tabelas no banco de dados
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

# Funçao - Adicionar um candidato ao banco de dados
def adicionar_candidato(nome, email, experiencia, curriculo):
    cursor.execute('INSERT INTO Candidato (Nome, E_mail, Experiencia, Curriculo) VALUES (?, ?, ?, ?)',
                   (nome, email, experiencia, curriculo))
    conn.commit()
    return cursor.lastrowid

# Funçao - Adicionar um recrutador ao banco de dados
def adicionar_recrutador(nome, empresa, contato):
    cursor.execute('INSERT INTO Recrutador (Nome, Empresa, Contato) VALUES (?, ?, ?)',
                   (nome, empresa, contato))
    conn.commit()
    return cursor.lastrowid

# Funçao - Adicionar uma vaga ao banco de dados
def adicionar_vaga(titulo, descricao, empresa, salario, requisitos):
    cursor.execute('INSERT INTO Vagas (Titulo, Descricao, Empresa, Salario, Requisitos) VALUES (?, ?, ?, ?, ?)',
                   (titulo, descricao, empresa, salario, requisitos))
    conn.commit()
    return cursor.lastrowid

# Funçao - Fazer upload de um currículo em PDF
def fazer_upload_curriculo():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        with open(file_path, 'rb') as file:
            return file.read()
    return None

# Funçao - Criar o perfil do candidato
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

# Funçao - Criar o perfil do recrutador
def criar_perfil_recrutador():
    nome = nome_entry.get()
    empresa = empresa_entry.get()
    contato = contato_entry.get()
    
    if nome and empresa and contato:
        recrutador_id = adicionar_recrutador(nome, empresa, contato)
        messagebox.showinfo("Sucesso", f"Perfil de Recrutador criado com sucesso (ID: {recrutador_id})")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos")

# Funçao - Criar uma vaga
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

# Funçao - Listar candidatos do banco de dados
def listar_candidatos():
    cursor.execute("SELECT ID_cand, Nome FROM Candidato")
    candidatos = cursor.fetchall()
    return candidatos

# Funçao - Listar vagas do banco de dados
def listar_vagas():
    cursor.execute("SELECT ID_vaga, Titulo FROM Vagas")
    vagas = cursor.fetchall()
    return vagas

# Funçao - Exibir a lista de candidatos em um Listbox
def exibir_lista_candidatos():
    candidatos = listar_candidatos()
    listbox.delete(0, tk.END)  # Limpa a lista existente
    for candidato in candidatos:
        listbox.insert(tk.END, f"{candidato[0]} - {candidato[1]}")

# Funçao - Exibir a lista de vagas em um Listbox
def exibir_lista_vagas():
    vagas = listar_vagas()
    listbox.delete(0, tk.END)  # Limpa a lista existente
    for vaga in vagas:
        listbox.insert(tk.END, f"{vaga[0]} - {vaga[1]}")

# Funçao - Validar email
def validar_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True

# Funçao - Abrir a interface do candidato
def abrir_interface_candidato():
    candidato_window = tk.Toplevel(root)
    candidato_window.title("DEVConnect - Candidato")

    # Labels e campos de entrada
    tk.Label(candidato_window, text="Nome:").pack()
    global nome_entry
    nome_entry = tk.Entry(candidato_window)
    nome_entry.pack()

    tk.Label(candidato_window, text="E-mail:").pack()
    global email_entry
    email_entry = tk.Entry(candidato_window)
    email_entry.pack()

    tk.Label(candidato_window, text="Experiência:").pack()
    global experiencia_text
    experiencia_text = tk.Text(candidato_window, height=5, width=40)
    experiencia_text.pack()

    # Botão - Fazer upload de currículo
    upload_button = tk.Button(candidato_window, text="Fazer Upload de Currículo (PDF)", command=fazer_upload_curriculo)
    upload_button.pack()

    # Botão - Criar o perfil do candidato
    criar_perfil_button = tk.Button(candidato_window, text="Criar Perfil de Candidato", command=criar_perfil_candidato)
    criar_perfil_button.pack()

    # Botão - Listar vagas
    listar_vagas_button = tk.Button(recrutador_window, text="Listar Vagas", command=exibir_lista_vagas)
    listar_vagas_button.pack()

    # Botão - Fechar a janela do candidato
    fechar_button = tk.Button(candidato_window, text="Fechar", command=candidato_window.destroy)
    fechar_button.pack()


# Funçao - Abrir a interface do recrutador
def abrir_interface_recrutador():
    recrutador_window = tk.Toplevel(root)
    recrutador_window.title("DEVConnect - Recrutador")

    # Labels e campos de entrada
    tk.Label(recrutador_window, text="Nome:").pack()
    global nome_entry
    nome_entry = tk.Entry(recrutador_window)
    nome_entry.pack()

    tk.Label(recrutador_window, text="Empresa:").pack()
    global empresa_entry
    empresa_entry = tk.Entry(recrutador_window)
    empresa_entry.pack()

    tk.Label(recrutador_window, text="Contato:").pack()
    global contato_entry
    contato_entry = tk.Entry(recrutador_window)
    contato_entry.pack()

    # Botão - Criar o perfil do recrutador
    criar_perfil_button = tk.Button(recrutador_window, text="Criar Perfil de Recrutador", command=criar_perfil_recrutador)
    criar_perfil_button.pack()

    # Botão - Fechar a janela do recrutador
    fechar_button = tk.Button(recrutador_window, text="Fechar", command=recrutador_window.destroy)
    fechar_button.pack()

    # Botão - Listar candidatos
    listar_candidatos_button = tk.Button(candidato_window, text="Listar Candidatos", command=exibir_lista_candidatos)
    listar_candidatos_button.pack()

    # Botão - Listar vagas
    listar_vagas_button = tk.Button(recrutador_window, text="Listar Vagas", command=exibir_lista_vagas)
    listar_vagas_button.pack()

# Funçao - Abrir a interface de vagas
def abrir_interface_vagas():
    vagas_window = tk.Toplevel(root)
    vagas_window.title("DEVConnect - Vagas")

    # Labels e campos de entrada
    tk.Label(vagas_window, text="Título da Vaga:").pack()
    global titulo_entry
    titulo_entry = tk.Entry(vagas_window)
    titulo_entry.pack()

    tk.Label(vagas_window, text="Descrição da Vaga:").pack()
    global descricao_text
    descricao_text = tk.Text(vagas_window, height=5, width=40)
    descricao_text.pack()

    tk.Label(vagas_window, text="Empresa:").pack()
    global empresa_entry
    empresa_entry = tk.Entry(vagas_window)
    empresa_entry.pack()

    tk.Label(vagas_window, text="Salário:").pack()
    global salario_entry
    salario_entry = tk.Entry(vagas_window)
    salario_entry.pack()

    tk.Label(vagas_window, text="Requisitos:").pack()
    global requisitos_text
    requisitos_text = tk.Text(vagas_window, height=5, width=40)
    requisitos_text.pack()

    # Botão - Criar uma vaga
    criar_vaga_button = tk.Button(vagas_window, text="Criar Vaga", command=criar_vaga)
    criar_vaga_button.pack()

    # Botão - Fechar a janela de vagas
    fechar_button = tk.Button(vagas_window, text="Fechar", command=vagas_window.destroy)
    fechar_button.pack()

    # Botão - Listar vagas
    listar_vagas_button = tk.Button(vagas_window, text="Listar Vagas", command=exibir_lista_vagas)
    listar_vagas_button.pack()

    # Lista de vagas e candidatos
    global listbox
    listbox = tk.Listbox(vagas_window, selectmode=tk.SINGLE, width=60, height=15)
    listbox.pack()

# Funçao - Fechar a janela do candidato
def fechar_janela_candidato():
    candidato_window.destroy()

# Funçao - Fechar a janela de vagas
def fechar_janela_vagas():
    vagas_window.destroy()

# Funçao - Listar candidatos no Listbox
def exibir_lista_candidatos():
    candidato_window = tk.Toplevel(root)
    candidato_window.title("Lista de Candidatos")

    # Lista de candidatos
    listbox = tk.Listbox(candidato_window, selectmode=tk.SINGLE, width=60, height=15)
    listbox.pack()

    candidatos = listar_candidatos()
    for candidato in candidatos:
        listbox.insert(tk.END, f"{candidato[0]} - {candidato[1]}")

# Funçao - Listar vagas no Listbox
def exibir_lista_vagas():
    vagas_window = tk.Toplevel(root)
    vagas_window.title("Lista de Vagas")

    # Lista de vagas
    listbox = tk.Listbox(vagas_window, selectmode=tk.SINGLE, width=60, height=15)
    listbox.pack()

    vagas = listar_vagas()
    for vaga in vagas:
        listbox.insert(tk.END, f"{vaga[0]} - {vaga[1]}")

# Interface principal
root = tk.Tk()
root.title("DEVConnect")

# Botões - Acessar as interfaces
candidato_button = tk.Button(root, text="Candidato", command=abrir_interface_candidato)
recrutador_button = tk.Button(root, text="Recrutador", command=abrir_interface_recrutador)
vagas_button = tk.Button(root, text="Vagas", command=abrir_interface_vagas)


candidato_button.pack()
recrutador_button.pack()
vagas_button.pack()

root.mainloop()

# Fechar a conexão com o banco de dados
conn.close()
