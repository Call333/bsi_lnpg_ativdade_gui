from tkinter import *
from db import ler_dados

def listarPorNome(e):
    def buscar(e):
        data = ler_dados()
        lb=Listbox(window, height=5, width=60, selectmode='single')
        print(len(entryVar.get()), 'Fora do For')
        for a in data:
            if(entryVar.get().lower() in a[0].lower()):
                # listaBuscas.append(a)
                lb.insert(END,a)
                lb.place(x=150, y=100)
                print(len(entryVar.get()), 'Dentro do for')

    # listaBuscas = []
    window = Tk()
    entryVar = StringVar()
    window.geometry('600x400')
    
    entry = Entry(window, textvariable=entryVar, width=25)
    busca = Button(window, text='Buscar')
    busca.bind('<Button-1>', buscar)

    entry.pack()
    entry.place(x=50, y=70)

    busca.pack()
    busca.place(x=50, y=100)

    window.mainloop()

listarPorNome(1)