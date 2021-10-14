# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 18:29:35 2021

Exercício 1
Escreva um programa que receba um número natural n na entrada e imprima  n! (fatorial) na saída.

Exemplo:
Digite o valor de n: 5
120
Dica: lembre-se que o fatorial de 0 vale 1

@author: Raphael Aguiar
"""
n = int(input("Digite o número a ter os fatoriais somados: "))

if n == 0:
    print("1")

else:
    fatorial = n
    while fatorial != 1:
        n = n*(fatorial-1)
        fatorial = fatorial-1
    print(n)