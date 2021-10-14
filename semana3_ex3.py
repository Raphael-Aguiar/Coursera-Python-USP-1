# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:33:43 2021

Exercícios 3 - FizzBuzz parcial, parte 2
Receba um número inteiro na entrada e imprima
Buzz
se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

@author: Raphael Aguiar
"""

n=int(input("Digite um número: "))
if n%5 == 0:
    print("Buzz")
else:
    print(n)