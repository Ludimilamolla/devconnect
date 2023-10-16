import tkinter as tk

# Funções para abrir as interfaces específicas
def abrir_interface_candidato():
    candidato_window = tk.Toplevel(root)
    candidato_window.title("Candidato")
    # Inclua aqui a interface do candidato
    
def abrir_interface_recrutador():
    recrutador_window = tk.Toplevel(root)
    recrutador_window.title("Recrutador")
    # Inclua aqui a interface do recrutador

def abrir_interface_vagas():
    vagas_window = tk.Toplevel(root)
    vagas_window.title("Vagas")
    # Inclua aqui a interface de vagas

# Interface principal
root = tk.Tk()
root.title("DEVConnect")

# Botões para acessar as interfaces
candidato_button = tk.Button(root, text="Candidato", command=abrir_interface_candidato)
recrutador_button = tk.Button(root, text="Recrutador", command=abrir_interface_recrutador)
vagas_button = tk.Button(root, text="Vagas", command=abrir_interface_vagas)

candidato_button.pack()
recrutador_button.pack()
vagas_button.pack()

root.mainloop()
