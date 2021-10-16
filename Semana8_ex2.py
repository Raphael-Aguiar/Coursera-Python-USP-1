# Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.
def soma_elementos(lista):
    i = 0
    for n in lista:
        i = i + n
    return i