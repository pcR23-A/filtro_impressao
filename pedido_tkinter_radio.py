import tkinter as tk
from tkinter import ttk

def subfiltros():
    tamanho = tamanho_var.get()
    cores = int(cores_var.get())
    substrato = substrato_var.get().strip().lower()
    qtd = int(qtd_entry.get())
    
    if qtd <= 0:
        result_label.config(text="Quantidade de rótulos deve ser maior que zero.")
        return

    if cores <= 0:
        result_label.config(text="Número de cores deve ser maior ou igual a zero.")
        return

    if cores <= 5 and (substrato == 'casca' or substrato == 'liso'):
        result_label.config(text='O pedido pode ser impresso nas máquinas KBA 1, KBA 2, KBA 4, KBA 5, KBA 6')
    elif cores <= 5 and substrato == 'metalizado':
        result_label.config(text='O pedido deverá ser impresso na KBA 2')
    elif cores <= 5 and substrato == 'couche':
        result_label.config(text='O pedido deverá ser impresso na KBA 3')
    elif cores == 6 and (substrato == 'casca' or substrato == 'liso'):
        result_label.config(text='O pedido pode ser impresso nas máquinas KBA 1, KBA 4, KBA 6, KBA 7')
    elif cores <= 6 and substrato == 'transparente':
        result_label.config(text='O pedido pode ser impresso nas máquinas KBA 5, KBA 6')
    elif cores == 7 and (substrato == 'casca' or substrato == 'liso' or substrato == 'transparente'):
        result_label.config(text='O pedido deverá ser impresso na máquina KBA 5')
    else:
        result_label.config(text='Algo pode estar incorreto/Remanejar Cores')

def main():
    balde = balde_var.get()
    
    if balde == 1:
        min_value.set(60000)
        subfiltros()
    elif balde == 2:
        min_value.set(30000)
        subfiltros()
    elif balde == 3:
        min_value.set(15000)
        subfiltros()
    else:
        result_label.config(text="Selecione um tamanho de balde válido.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Filtro de Impressão")
root.iconbitmap(r"C:\Users\Administrador\Downloads\html\html\filtro\logo.ico")

# Definir o tamanho da janela e torná-la não redimensionável
root.geometry("500x680")
root.resizable(False, False)

balde_var = tk.IntVar()
tamanho_var = tk.IntVar()
cores_var = tk.StringVar()
min_value = tk.IntVar()
substrato_var = tk.StringVar()

# Centralização dos elementos
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Interface para selecionar o balde
ttk.Label(root, text="Selecione o tamanho do balde:").grid(column=0, row=0, padx=10, pady=5, columnspan=2)
ttk.Radiobutton(root, text="(BX500, BX1000)", variable=balde_var, value=1).grid(column=0, row=1, padx=10, pady=5, columnspan=2)
ttk.Radiobutton(root, text="(3.2, 3.5, 3.6N, 3.6MD, 3.6R)", variable=balde_var, value=2).grid(column=0, row=2, padx=10, pady=5, columnspan=2)
ttk.Radiobutton(root, text="(7.2, 12N, 20L)", variable=balde_var, value=3).grid(column=0, row=3, padx=10, pady=5, columnspan=2)

# Linha separadora
ttk.Separator(root, orient='horizontal').grid(column=0, row=4, columnspan=2, sticky='ew', pady=10)

# Interface para selecionar o tamanho do rótulo
ttk.Label(root, text="Selecione o tamanho do rótulo:").grid(column=0, row=5, padx=10, pady=5, columnspan=2)
ttk.Radiobutton(root, text="Grande", variable=tamanho_var, value=1).grid(column=0, row=6, padx=10, pady=5, columnspan=2)
ttk.Radiobutton(root, text="Médio", variable=tamanho_var, value=2).grid(column=0, row=7, padx=10, pady=5, columnspan=2)
ttk.Radiobutton(root, text="Pequeno", variable=tamanho_var, value=3).grid(column=0, row=8, padx=10, pady=5, columnspan=2)

# Linha separadora
ttk.Separator(root, orient='horizontal').grid(column=0, row=9, columnspan=2, sticky='ew', pady=10)

# Interface para selecionar o substrato
ttk.Label(root, text="Selecione o substrato a ser utilizado:").grid(column=0, row=10, padx=10, pady=5, columnspan=2)
ttk.Radiobutton(root, text="Casca", variable=substrato_var, value='casca').grid(column=0, row=11, padx=10, pady=5)
ttk.Radiobutton(root, text="Liso", variable=substrato_var, value='liso').grid(column=1, row=11, padx=10, pady=5)
ttk.Radiobutton(root, text="Metalizado", variable=substrato_var, value='metalizado').grid(column=0, row=12, padx=10, pady=5)
ttk.Radiobutton(root, text="Couche", variable=substrato_var, value='couche').grid(column=1, row=12, padx=10, pady=5)
ttk.Radiobutton(root, text="Transparente", variable=substrato_var, value='transparente').grid(column=0, row=13, padx=10, pady=5)

# Linha separadora
ttk.Separator(root, orient='horizontal').grid(column=0, row=14, columnspan=2, sticky='ew', pady=10)

# Interface para selecionar o número de cores
ttk.Label(root, text="Selecione o número de cores a serem utilizadas:").grid(column=0, row=15, padx=10, pady=5, columnspan=2)
cores_dropdown = ttk.Combobox(root, textvariable=cores_var)
cores_dropdown['values'] = [str(i) for i in range(1,8)]
cores_dropdown.grid(column=0, row=16, columnspan=2, padx=10, pady=5)

# Linha separadora
ttk.Separator(root, orient='horizontal').grid(column=0, row=17, columnspan=2, sticky='ew', pady=10)

# Entrada para a quantidade de rótulos
ttk.Label(root, text="Digite a quantidade de rótulos a serem impressos:").grid(column=0, row=18, padx=10, pady=5, columnspan=2)
qtd_entry = ttk.Entry(root)
qtd_entry.grid(column=0, row=19, columnspan=2, padx=10, pady=5)

# Linha separadora
ttk.Separator(root, orient='horizontal').grid(column=0, row=20, columnspan=2, sticky='ew', pady=10)

# Botão para executar o filtro
ttk.Button(root, text="Executar", command=main).grid(column=0, row=21, columnspan=2, padx=10, pady=10)

# Label para exibir o resultado
result_label = ttk.Label(root, text="")
result_label.grid(column=0, row=22, columnspan=2, padx=10, pady=10)

root.mainloop()
