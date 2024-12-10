import tkinter as tk

import funcs
from tkinter import ttk


# Definição de funções
# Função disparada pelo evento FocusIn para criaçao de linha de ingredientes
def add_lingrev(event):
    if event.widget == arraylinhaingrediente[len(arraylinhaingrediente) - 1].entry_ingrediente:
        add_lingr()


# Função que cria linha do sector ingredientes
def add_lingr():
    var_ingrediente = tk.StringVar()
    var_quantidade = tk.DoubleVar()

    label_ingrediente = ttk.Label(master=frameingr, text='Ingrediente: ', font=("Arial", 20))
    label_ingrediente.grid(row=len(arraylinhaingrediente) + 1, column=0)
    entry_ingrediente = ttk.Entry(master=frameingr, textvariable=var_ingrediente, width=15, font=("Arial", 20))
    entry_ingrediente.grid(row=len(arraylinhaingrediente) + 1, column=1)
    lista_autocomplete = tk.Listbox(master=frameingr, width=15, font=("Arial", 20))

    label_quantidade = ttk.Label(master=frameingr, text='Quantidade: ', font=("Arial", 20))
    label_quantidade.grid(row=len(arraylinhaingrediente) + 1, column=2)
    entry_quantidade = ttk.Entry(master=frameingr, textvariable=var_quantidade, width=5, font=("Arial", 20))
    entry_quantidade.grid(row=len(arraylinhaingrediente) + 1, column=3)

    # Guardar informação da linha do ingrediente num objecto desse tipo
    linhaingredientes = funcs.LinhasIngredientes(label_ingrediente, entry_ingrediente, var_ingrediente,
                                                 label_quantidade, entry_quantidade,
                                                 var_quantidade)
    arraylinhaingrediente.append(linhaingredientes)

    # Binds dos objetos
    entry_ingrediente.bind('<FocusIn>', add_lingrev)
    entry_ingrediente.bind('<FocusOut>', rm_lingr)

    # Bind do autocomplete, ainda com bug
    entry_ingrediente.bind('<KeyRelease>', lambda event: funcs.on_key_release(event, prato, lista_autocomplete, db,
                                                                              linhaingredientes, arrayvarnutrientes))

    lista_autocomplete.bind("<Double-Button-1>", lambda event: funcs.on_select(event, prato, linhaingredientes,
                                                                               lista_autocomplete, arrayvarnutrientes))

    entry_quantidade.bind('<KeyRelease>',
                          lambda event: funcs.on_quantidade_key_release(event, prato, linhaingredientes,
                                                                        arrayvarnutrientes, entry_quantidade))


# Função que remove linha de ingredientes quando o entry é descelecionado e é penultimo e vazio
def rm_lingr(event):
    if (event.widget == arraylinhaingrediente[len(arraylinhaingrediente) - 2].entry_ingrediente) and (
            len(arraylinhaingrediente) > 5) and (
            arraylinhaingrediente[len(arraylinhaingrediente) - 2].entry_ingrediente.get() == ''):
        for linhaingrediente in arraylinhaingrediente[(len(arraylinhaingrediente) - 1):]:
            linhaingrediente.label_ingrediente.destroy()
            linhaingrediente.entry_ingrediente.destroy()
            linhaingrediente.label_quantidade.destroy()
            linhaingrediente.entry_quantidade.destroy()
            arraylinhaingrediente.remove(linhaingrediente)


# Criação da janela e caracteristicas da janela
janela = tk.Tk()
janela.title("Gestão nutricional")
janela.geometry("1113x744+461+103")

# Criação de objetos (Nutrientes, linhas da frame dos ingredientes, base de dados e prato)
var_energia = tk.DoubleVar()
var_proteinas = tk.DoubleVar()
var_hidratos = tk.DoubleVar()
var_acucar = tk.DoubleVar()
var_lipidos_total = tk.DoubleVar()
var_lipidos_saturados = tk.DoubleVar()
var_lipidos_mono = tk.DoubleVar()
var_lipidos_poli = tk.DoubleVar()
var_fibra = tk.DoubleVar()
var_sodio = tk.DoubleVar()
arrayvarnutrientes = funcs.ListaNutrientes(var_energia, var_proteinas, var_hidratos, var_acucar, var_lipidos_total,
                                           var_lipidos_saturados,
                                           var_lipidos_mono, var_lipidos_poli, var_fibra, var_sodio)

arraylinhaingrediente = []

db = funcs.Database()
db.loaddatabase()
prato = funcs.Prato('Prato1', db.get())

# Criação dos componentes na janela
# Dividir a janela em 2 sectores
frameesq = ttk.Frame(master=janela, borderwidth=5, relief=tk.GROOVE)
frameesq.pack(side='left', fill='both', expand=True, pady=10, padx=5)

framedir = ttk.Frame(master=janela, borderwidth=5, relief=tk.GROOVE)
framedir.pack(side='left', fill='both', expand=True, pady=10, padx=5)

# Preencher sector dos ingredientes
titingr = ttk.Label(master=frameesq, text="Ingredientes do prato")
titingr.pack(side='top')

frameingr = ttk.Frame(master=frameesq, borderwidth=5, relief=tk.GROOVE)
frameingr.pack(side='top', fill='both', expand=True, pady=10, padx=5)

# Chama a função para criar linhas de ingredientes
for i in range(5):
    add_lingr()

button = tk.Button(master=frameesq, text="Imprimir", command=lambda: funcs.imprime_prato(arrayvarnutrientes, prato))
button.pack(side='bottom', pady=10, padx=5)

# Preencher sector dos nutrientes
labnutrientes = ttk.Label(master=framedir, text="Nutrientes do prato")
labnutrientes.pack(side='top')

frametabnutri = ttk.Frame(master=framedir, borderwidth=5, relief=tk.GROOVE)
frametabnutri.pack(side='top', fill='both', expand=True, pady=10, padx=5)

label_energia = ttk.Label(master=frametabnutri, text="Energia (Kcal)", font=("Arial", 15))
label_energia.grid(row=0, column=0)
label_energia1 = ttk.Label(master=frametabnutri, textvariable=var_energia, font=("Arial", 15))
label_energia1.grid(row=0, column=1)

label_proteinas = ttk.Label(master=frametabnutri, text="Proteinas (g)", font=("Arial", 15))
label_proteinas.grid(row=1, column=0)
label_proteinas1 = ttk.Label(master=frametabnutri, textvariable=var_proteinas, font=("Arial", 15))
label_proteinas1.grid(row=1, column=1)

label_hidratos = ttk.Label(master=frametabnutri, text="Hidratos de carbono (g)", font=("Arial", 15))
label_hidratos.grid(row=2, column=0)
label_hidratos1 = ttk.Label(master=frametabnutri, textvariable=var_hidratos, font=("Arial", 15))
label_hidratos1.grid(row=2, column=1)

label_acucar = ttk.Label(master=frametabnutri, text="Açucar (g)", font=("Arial", 15))
label_acucar.grid(row=3, column=0)
label_acucar1 = ttk.Label(master=frametabnutri, textvariable=var_acucar, font=("Arial", 15))
label_acucar1.grid(row=3, column=1)

label_lipidos_total = ttk.Label(master=frametabnutri, text="Lipidos total (g)", font=("Arial", 15))
label_lipidos_total.grid(row=4, column=0)
label_lipidos_total1 = ttk.Label(master=frametabnutri, textvariable=var_lipidos_total, font=("Arial", 15))
label_lipidos_total1.grid(row=4, column=1)

label_lipidos_saturados = ttk.Label(master=frametabnutri, text="Lipidos saturados (g)", font=("Arial", 15))
label_lipidos_saturados.grid(row=5, column=0)
label_lipidos_saturados1 = ttk.Label(master=frametabnutri, textvariable=var_lipidos_saturados, font=("Arial", 15))
label_lipidos_saturados1.grid(row=5, column=1)

label_lipidos_mono = ttk.Label(master=frametabnutri, text="Lipidos monoinsaturados (g)", font=("Arial", 15))
label_lipidos_mono.grid(row=6, column=0)
label_lipidos_mono1 = ttk.Label(master=frametabnutri, textvariable=var_lipidos_mono, font=("Arial", 15))
label_lipidos_mono1.grid(row=6, column=1)

label_lipidos_poli = ttk.Label(master=frametabnutri, text="Lipidos polinsaturados (g)", font=("Arial", 15))
label_lipidos_poli.grid(row=7, column=0)
label_lipidos_poli1 = ttk.Label(master=frametabnutri, textvariable=var_lipidos_poli, font=("Arial", 15))
label_lipidos_poli1.grid(row=7, column=1)

label_fibra = ttk.Label(master=frametabnutri, text="Fibra (g)", font=("Arial", 15))
label_fibra.grid(row=8, column=0)
label_fibra1 = ttk.Label(master=frametabnutri, textvariable=var_fibra, font=("Arial", 15))
label_fibra1.grid(row=8, column=1)

label_sodio = ttk.Label(master=frametabnutri, text="Sódio (mg)/Sal (g)", font=("Arial", 15))
label_sodio.grid(row=9, column=0)
label_sodio1 = ttk.Label(master=frametabnutri, textvariable=var_sodio, font=("Arial", 15))
label_sodio1.grid(row=9, column=1)

# Colocar a janela em loop
janela.mainloop()
