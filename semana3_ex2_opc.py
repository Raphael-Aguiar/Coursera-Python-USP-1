# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 17:24:56 2021

Exercício 2 - Desafio da videoaula
Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.

O programa deve receber os parâmetros  a a,  b b, e  c c da equação  ax^2 + bx + c ax2+bx+c, respectivamente, e imprimir o resultado na saída da seguinte maneira:

Quando não houver raízes reais imprima:

esta equação não possui raízes reais

Quando houver apenas uma raiz (ou seja, uma raiz com multiplicidade 2) imprima:

a raiz desta equação é X

ou

a raiz dupla desta equação é X

onde X é o valor da raiz dupla

Quando houver duas raízes reais imprima:

as raízes da equação são X e Y

onde X e Y são os valor das raízes.

Além disso, no caso de existirem 2 raízes reais distintas, elas devem ser impressas em ordem crescente. Exemplos:

as raízes da equação são 1.0 e 2.0

as raízes da equação são -2.0 e 0.0

@author: Raphael Aguiar
"""

a=float(input("Digite o número 'a' da equação: "))
b=float(input("Digite o número 'b' da equação: "))
c=float(input("Digite o número 'c' da equação: "))

delta=(b**2)-(4*a*c)
if delta < 0:
    print("esta equação não possui raízes reais")
else:
    import math
    raiz1=(-b+math.sqrt(delta))/(2*a)   
    if delta==0:       
        print("a raiz dupla desta equação é",raiz1)
    else:
        raiz2=(-b-math.sqrt(delta))/(2*a)
        if raiz1 < raiz2:
            print("as raízes da equação são",raiz1,"e",raiz2)
        else:
            print("as raízes da equação são",raiz2,"e",raiz1)