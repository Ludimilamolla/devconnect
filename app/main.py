import tkinter as tk

import candidato_interface
import recrutador_interface
import vagas_interface
import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('recrutamento.db')

# Funções para abrir as interfaces
def abrir_interface_candidato():
    candidato_interface.abrir_interface_candidato(conn)

def abrir_interface_recrutador():
    recrutador_interface.abrir_interface_recrutador(conn)

def abrir_interface_vagas():
    vagas_interface.abrir_interface_vagas(conn)

# Função para criar a página de menu principal
def criar_menu_principal():
    menu_principal = tk.Tk()
    menu_principal.title("DEVConnect - Menu Principal")

    candidato_button = tk.Button(menu_principal, text="Candidato", command=abrir_interface_candidato)
    candidato_button.pack()

    recrutador_button = tk.Button(menu_principal, text="Recrutador", command=abrir_interface_recrutador)
    recrutador_button.pack()

    vagas_button = tk.Button(menu_principal, text="Vagas", command=abrir_interface_vagas)
    vagas_button.pack()

    menu_principal.mainloop()

# Criar a página de menu principal
criar_menu_principal()

# Fechar a conexão com o banco de dados ao encerrar o aplicativo
conn.close()
