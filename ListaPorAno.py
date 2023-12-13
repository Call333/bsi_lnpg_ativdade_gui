from tkinter import *
from tkinter import ttk
import db

def listaPorAno():
    def busca_por_ano(e):
        data = db.ler_dados()
        lb = Listbox(mainframe, height=5, width=60, selectmode='single')
        
        print(len(data))
        for a in data:
            if(valueRadios.get() == 0):
                if(a[1] == cb.get()):
                    lb.insert(END,a)
                    lb.grid(column=4, row=1)
            elif(valueRadios.get() == 1):
                if(a[1] <= cb.get()):
                    lb.insert(END,a)
                    lb.grid(column=4, row=1)
            elif(valueRadios.get() == 2):
                if(a[1] >= cb.get()):
                    lb.insert(END,a)
                    lb.grid(column=4, row=1)

    win = Tk()
    win.title('Listagem por ano')
    win.geometry('600x400')
    mainframe = ttk.Frame(win, padding='20')
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    win.columnconfigure(0, weight=1)
    win.rowconfigure(0, weight=1)

    botao = Button(win, text="Clique Aqui!")
    botao.bind('<Button-1>', busca_por_ano)
    botao.grid(column=2, row=5)
    
    anos = []

    a = 2020
    while(a >= 1900):
        anos.append(a)
        a -= 1

    cb = ttk.Combobox(mainframe, values=anos)
    cb.current(0)
    cb.grid(column=2, row=1)

    valueRadios = IntVar(value=0)
    r1 = Radiobutton(mainframe, text='Igual ao ano', variable=valueRadios,  value=0).grid(column=2, row=2)
    r2 = Radiobutton(mainframe, text='Anterior ao ano', variable=valueRadios, value=1).grid(column=2, row=3)
    r2 = Radiobutton(mainframe, text='Posterior ao ano', variable=valueRadios, value=2).grid(column=2, row=4)

    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=15, pady=5)

    win.mainloop()

listaPorAno()