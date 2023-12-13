

def ler_dados():
    arquivo = open("data.txt", "r", encoding="utf-8")
    dados = arquivo.read()
    listaDados = dados.split("\n")

    for d in listaDados:
        listaDeAlbuns.append(d.split(" | "))

    for i in listaDeAlbuns:
        if(i == ['']):
            listaDeAlbuns.remove(i)
    arquivo.close()

listaDeAlbuns = []

def cadastrarAlbum():
    nome = input("Digite o nome do álbum: ")
    anoLancamento = int(input("Digte o ano do lançamento: "))
    BandaOuArtista = input("Digite o nome da banda/artista: ")
    albumDeLancamento = int(input("Digite\n\t1 - Sim\n\t2 - Não: "))

    if(albumDeLancamento == 1):
        arquivo = open("data.txt", "a", encoding="utf-8")
        arquivo.write(f"{nome}\t{anoLancamento}\t{BandaOuArtista}\t{True}\n")
        arquivo.close()

    elif(albumDeLancamento == 2):
        arquivo = open("data.txt", "a", encoding="utf-8")
        arquivo.write(f"{nome}\t{anoLancamento}\t{BandaOuArtista}\t{False}\n")
        arquivo.close()

def buscarAlbunsPorNome(nome):
    for a in listaDeAlbuns:
        if(nome.lower() in a[0].lower()):
            print(a)

def buscarAlbunsPeloAno(ano, simbolo):
    for a in listaDeAlbuns:
        if(simbolo == 1):
            if(int(a[1]) <= ano):
                print(a)
        elif(simbolo == 2):
            if(int(a[1]) >= ano):
                print(a)
        elif(simbolo == 3):
            if(int(a[1]) == ano):
                print(a)

def menu():
    while(True):
        print("*** Sistemas de Cadastro e Consulta de Álbuns ***")
        print("")
        print("1 - Cadastrar Álbum")
        print("2 - Buscar Àlbum por nome")
        print("3 - Buscar Álbum por ano")
        print("")
        try:
            print("Digite aqui o número correspondente a opção desejada: ")
            res = int(input(""))

            if(res == 1):
                cadastrarAlbum()
            elif(res == 2):
                nomeSearch = input("Nome ou cadeia de caracteres a ser pesquisado referente ao álbum: ")
                buscarAlbunsPorNome(nomeSearch)
            elif(res == 3):
                anoSearch = int(input("Ano a ser pesquisado: "))
                simbolo = int(input(f"Deseja buscar como:\n\t1 - Anterior a {anoSearch}\n\t2 - Posterior a {anoSearch}\n\t3 - Igual a {anoSearch}\n"))
                buscarAlbunsPeloAno(anoSearch, simbolo)
            elif(res == 4):
                break
        except:
            print("\t*Mengagem:O valor digitado não é um número")
ler_dados()
menu()