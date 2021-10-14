# -*- coding: utf-8 -*-

"""
Exercício 1 - Par ou ímpar?
Receba um número inteiro na entrada e imprima
par 
quando o número for par ou
ímpar
quando o número for ímpar.

n1=int(input("Digite um número: "))
if n1 % 2 == 0:
    print("par")
else:
    print("í­mpar")
    
"""
n1=int(input("Digite um número: "))
if n1 % 2 != 0:
    print("ímpar")
else:
    print("par")