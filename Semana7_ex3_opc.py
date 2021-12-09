# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 09:43:52 2021

Primos
Escreva a função n_primos que recebe como argumento um número inteiro maior ou
igual a 2 como parâmetro e devolve a quantidade de números primos que existem
entre 2 e n (incluindo 2 e, se for o caso, n).

Ex:
>> >n_primos(2)
1
>>> n_primos(4)
2
>>> n_primos(121)
30

@author: Raphael Aguiar
"""

def éPrimo(k):
    contador = resto = 2
    primo = True

    while contador < k:
        resto = k % contador
        contador = contador + 1
        if resto == 0:
            primo = False
    return primo


def n_primos(x):
    contador_primo = 1
    lista = list(range(3, x+1))
    for numero in lista:
       if éPrimo(numero):
           contador_primo += 1
    return contador_primo


print(n_primos(20))




