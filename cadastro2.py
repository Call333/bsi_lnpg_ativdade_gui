from tkinter import *
from tkinter import ttk
from listagemSimples import listagemSimples
from db import escrever_dados
from ListagemPorNome import *
from ListaPorAno import listaPorAno

def tela_cadastro():
    def w(e):
        escrever_dados(album.get(), ano.get(), autoria.get(), primeiro_album.get())
        
        album.set('')
        ano.set('')
        autoria.set('')

    janela = Tk()
    janela.title('Tela de Cadastro')
    janela.geometry('600x300')

    mainframe = ttk.Frame(janela, padding='3 5 24 24')
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    janela.columnconfigure(0, weight=1)
    janela.rowconfigure(0, weight=1)

    album = StringVar()
    ano = StringVar()
    autoria = StringVar()
    primeiro_album = IntVar()

    album_label = ttk.Label(mainframe, text='Álbum: ').grid(column=1, row=1, sticky=(W, E))
    album_entry = ttk.Entry(mainframe, width=40, textvariable=album).grid(column=3, row=1, sticky=(W, E))

    ano_label = ttk.Label(mainframe, text='Ano do Lançamento: ').grid(column=1, row=2, sticky=(W, E))
    ano_entry = ttk.Entry(mainframe, textvariable=ano).grid(column=3, row=2, sticky=(W, E))

    autor_label = ttk.Label(mainframe, text='Autor: ').grid(column=1, row=3, sticky=(W, E))
    autor_entry = ttk.Entry(mainframe, textvariable=autoria).grid(column=3, row=3, sticky=(W, E))

    primeiro_album_label = ttk.Label(mainframe, text='Primeiro Álbum da Banda/Autor? ').grid(column=1, row=4,sticky=(E))
    primeiro_album_radio_sim = ttk.Radiobutton(mainframe, variable=primeiro_album, text='Sim', value=1).grid(column=2, row=4 ,sticky=E)
    primeiro_album_radio_nao = ttk.Radiobutton(mainframe, variable=primeiro_album, text='Não', value=0).grid(column=3, row=4 ,sticky=(E))

    btnCadastrar = Button(mainframe, text='Cadastrar')
    btnCadastrar.bind('<Button-1>', w)
    btnCadastrar.grid(column=3, row=5, sticky=E)

    btnListarAlbuns = Button(mainframe, text='Lista Albuns')
    btnListarAlbuns.bind('<Button-1>', listagemSimples)
    btnListarAlbuns.grid(column=2, row=5, sticky=E)

    # btnListarAlbuns = Button(mainframe, text='Lista Por Nome')
    # btnListarAlbuns.bind('<Button-1>', ListaPorAno.listaPorAno)
    # btnListarAlbuns.grid(column=2, row=6, sticky=E)

    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    janela.mainloop()

tela_cadastro()