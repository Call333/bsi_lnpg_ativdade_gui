path = 'data.txt'

def ler_dados():
    dadosLidos = []
    arq = open(path, 'r', encoding='utf-8')
    leitura = arq.read()
    dados = leitura.split('\n')

    for d in dados:
        dadosLidos.append(d.split(' | '))

    for b in dadosLidos:
        if(b == ['']):
            dadosLidos.remove(b)
    
    arq.close()
    return dadosLidos

def escrever_dados(album, ano, autoria, primeiro_album):
    arq = open(path, 'a', encoding='utf-8')
    arq.write(f'{album} | {ano} | {autoria} | {primeiro_album}\n')
    arq.close()

# escrever_dados('Homem torto', 2005, 'Não sei', 1)
