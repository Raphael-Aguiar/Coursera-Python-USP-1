# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:24:44 2021

Exercícios 2 - FizzBuzz parcial, parte 1
Receba um número inteiro na entrada e imprima 
Fizz
se o número for divisível por 3. Caso contrário, imprima o mesmo número que foi dado na entrada.

@author: Raphael Aguiar
"""

n=int(input("Digite um número: "))
if n%3 == 0:
    print("Fizz")
else:
    print(n)
