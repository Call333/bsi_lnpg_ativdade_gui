from tkinter import *
from tkinter import ttk
from db import ler_dados

def listagemSimples(e):
    listaDosAlbuns = ler_dados()

    listagem = Tk()
    listagem.title('Lista de Álbuns')

    listagem.geometry('600x700')

    mainframe = ttk.Frame(listagem, padding=('20'))
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    listagem.columnconfigure(0, weight=1)
    listagem.rowconfigure(0, weight=1)

    album_lbl = Label(mainframe, text='Álbum').grid(column=1, row=1, sticky=(E))
    ano_lancamento_lbl = Label(mainframe, text='Ano').grid(column=2, row=1, sticky=(E))
    autoria_lbl = Label(mainframe, text='Autor').grid(column=3, row=1, sticky=(E))
    primeiro_album_lbl = Label(mainframe, text='Lançamento').grid(column=4, row=1, sticky=(E))

    linha = 2
    coluna = 2

    for alb in listaDosAlbuns:
        album = StringVar(value=alb[0])
        ano_lancamento = StringVar(value=alb[1])
        autoria = StringVar(value=alb[2])
        primeiro_album = IntVar(value=alb[3])

        alb_lbl_dado = Label(mainframe, text=album.get()).grid(column=1, row=linha, sticky=(E))
        ano_lbl_dado = Label(mainframe, text=ano_lancamento.get()).grid(column=2, row=linha, sticky=(E))
        autor_lbl_dado = Label(mainframe, text=autoria.get()).grid(column=3, row=linha, sticky=(E))
        if(primeiro_album.get() == 1):
            lanca_lbl_dado = Label(mainframe, text='Sim').grid(column=4, row=linha, sticky=(E))
        elif(primeiro_album.get() == 0):
            lanca_lbl_dado = Label(mainframe, text='Não').grid(column=4, row=linha, sticky=(E))

        linha += 1

    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=15, pady=5)

    listagem.mainloop()

# listagemSimples(e=1)