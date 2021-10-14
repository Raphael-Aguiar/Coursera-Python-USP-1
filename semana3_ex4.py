# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:35:07 2021

Exercícios 4 - FizzBuzz parcial, parte 3
Receba um número inteiro na entrada e imprima
FizzBuzz
na saída se o número for divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

@author: Raphael Aguiar
"""

n=int(input("Digite um número: "))
if n%3 == 0 and n%5 == 0:
    print("FizzBuzz")
else:
    print(n)
