# Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. 
# A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.
# Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?

def remove_repetidos(lista):
    lista2 = []
    lista.sort()
    for obj in lista:
        if obj in lista and obj not in lista2:
            lista2.append(obj)
    return lista2

