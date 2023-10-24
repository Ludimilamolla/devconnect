import tkinter as tk

# ... (código) ...

# Função para exibir detalhes do candidato
def exibir_detalhes_candidato():
    selected_item = listbox.get(listbox.curselection())  # Obtém o item selecionado na lista
    candidato_id = int(selected_item.split()[0])  # Extrai o ID do candidato do item selecionado

    # Agora você pode buscar os detalhes desse candidato no banco de dados e exibir em uma nova janela
    candidato_detalhes = obter_detalhes_candidato(candidato_id)

    # Crie uma nova janela para exibir os detalhes do candidato
    detalhes_window = tk.Toplevel(root)
    detalhes_window.title(f"Detalhes do Candidato (ID: {candidato_id})")

    # Crie rótulos e exiba as informações detalhadas
    tk.Label(detalhes_window, text=f"ID: {candidato_id}").pack()
    tk.Label(detalhes_window, text=f"Nome: {candidato_detalhes['Nome']}").pack()
    tk.Label(detalhes_window, text=f"E-mail: {candidato_detalhes['E_mail']}").pack()
    tk.Label(detalhes_window, text=f"Experiência: {candidato_detalhes['Experiencia']}").pack()

# ... (código) ...

# Botão para exibir detalhes do candidato
exibir_detalhes_button = tk.Button(candidato_window, text="Exibir Detalhes do Candidato", command=exibir_detalhes_candidato)
exibir_detalhes_button.pack()

# ... (código) ...
