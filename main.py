from tkinter import *
from dbd import *

################# Cores usadas no projeto ##############

co0 = "#000000"  # preta
co1 = "#59656F"
co2 = "#feffff"  # branca
co3 = "#0074eb"  # azul
co4 = "#f04141"  # vermelho
co5 = "#59b356"  # verde
co6 = "#cdd1cd"  # cizenta

# criando janela principal
janela = Tk()
janela.resizable(width=FALSE, height=FALSE)
janela.geometry("500x225")
janela.title("To-do App")
janela.configure(background=co1)

# dividindo a janela em duas partes 
frame_esquerda = Frame(janela, width=300, height=200, bg=co2, relief="flat")
frame_esquerda.grid(row=0, column=0, sticky=NSEW)

frame_direita = Frame(janela, width=200, height=250, bg=co2, relief="flat")
frame_direita.grid(row=0, column=1, sticky=NSEW)

# dividindo o frame a esquerda em duas parte
frame_e_cima = Frame(frame_esquerda, width=300, height=50, bg=co2, relief="flat")
frame_e_cima.grid(row=0, column=0, sticky=NSEW)

frame_e_baixo = Frame(frame_esquerda, width=300, height=150, bg=co2, relief="flat")
frame_e_baixo.grid(row=1, column=0, sticky=NSEW)


def main(a):
    # novo 
    if a == "novo":
        for widget in frame_e_baixo.winfo_children():
            widget.destroy()

        def adicionar():
            tarefa_entry = entry.get()
            inserir([tarefa_entry])
            mostrar()
        
        lb = Label(frame_e_baixo, text="Insira nova tarefa", width=42, 
                height=5, pady=15, anchor=CENTER)
        lb.grid(row=0, column=0, sticky=NSEW)

        entry = Entry(frame_e_baixo, width=15)
        entry.grid(row=1, column=0, sticky=NSEW)

        b_adicionar = Button(frame_e_baixo, text="Adicionar", width=9, pady=10,
                height=1, bg=co6, fg=co0, font="8", anchor="center", relief=RAISED, command=adicionar)
        b_adicionar.grid(row=2, column=0, sticky=NSEW, pady=15)
        
    # atualizar 
    if a == "atualizar":
        for widget in frame_e_baixo.winfo_children():
            widget.destroy()

        def on():
            lb = Label(frame_e_baixo, text="Atualizar tarefa", width=42, 
                    height=5, pady=15, anchor=CENTER)
            lb.grid(row=0, column=0, sticky=NSEW)

            entry = Entry(frame_e_baixo, width=15)
            entry.grid(row=1, column=0, sticky=NSEW)

            v_slecionado = listbox.curselection()[0]
            palavra = listbox.get(v_slecionado)
            entry.insert(0, palavra)

            tarefas = selecionar()

            def alterar():
                for item in tarefas:
                    if palavra==item[1]:
                        nova=[entry.get(), item[0]]
                        atualizar(nova)
                        entry.delete(0, END)
                mostrar()

            b_alterar = Button(frame_e_baixo, text="Atualizar", width=9, pady=10,
                    height=1, bg=co6, fg=co0, font="8", anchor="center", relief=RAISED, command=alterar)
            b_alterar.grid(row=2, column=0, sticky=NSEW, pady=15)

        on()

# função remover
def remove():
    v_slecionado = listbox.curselection()[0]
    palavra = listbox.get(v_slecionado)
    tarefas = selecionar()

    for item in tarefas:
        if palavra == item[1]:
            deletar([item[0]])
    mostrar()



# criando botões novo, remover e atualizar
b_novo = Button(frame_e_cima, text="Novo", width=10, 
                height=1, bg=co3, fg="white", font="5", anchor="center", relief=RAISED, command=lambda: main('novo'))
b_novo.grid(row=0, column=0, sticky=NSEW, pady=1)

b_remover = Button(frame_e_cima, text="Remover", width=10, 
                height=1, bg=co4, fg="white", font="5", anchor="center", relief=RAISED, command=remove)
b_remover.grid(row=0, column=1, sticky=NSEW, pady=1)

b_atualizar = Button(frame_e_cima, text="Atualizar", width=10, 
                height=1, bg=co5, fg="white", font="5", anchor="center", relief=RAISED, command=lambda: main('atualizar'))
b_atualizar.grid(row=0, column=2, sticky=NSEW, pady=1)


# Adicionando Listbox e um Label
label = Label(frame_direita, text="Tarefas", width=37, height=1, pady=7, 
            padx=10, relief="flat", anchor=W, font=("Courier 20 bold"), fg=co0, bg=co2)
label.grid(row=0, column=0, sticky=NSEW, pady=1)

listbox = Listbox(frame_direita, font=("Courier 9 bold"), width=1)
listbox.grid(row=1, column=0, sticky=NSEW, pady=5)


# adicionando tarefa na listbox
def mostrar():
    listbox.delete(0, END)
    tarefas = selecionar()

    for item in tarefas:
        listbox.insert(END, item[1])







mostrar()

janela.mainloop()