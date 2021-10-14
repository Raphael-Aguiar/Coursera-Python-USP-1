# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 09:46:43 2021

Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

Exemplos de execução no shell de Python:
    
>>> vogal("a")
True
>>> vogal("b")
False
>>> vogal("E")
True

Os valores True e False devolvidos devem ser do tipo bool (booleanos), e não strings

Dica: Lembre-se que para passar uma vogal como parâmetro ela precisa ser um texto, ou seja, precisa estar entre aspas.

@author: Raphael Aguiar
"""
def vogal(x):
    y = str(x.upper())
    if y == "A" or y == "E" or y == "I" or y == "O" or y == "U":
        vogal = True
    else:
        vogal = False
    return vogal
    
