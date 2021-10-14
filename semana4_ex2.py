# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:53:09 2021

Exercício 2
Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

Exemplo:

Digite o valor de n: 5
1
3
5
7
9

@author: Raphael Aguiar
"""

n=(int(input("Digite um número inteiro positivo: ")))
ciclo = 1
marcador = 1
while marcador <= n:
    print(ciclo)
    ciclo = ciclo+2
    marcador = marcador + 1


"""
Resoluções alternativas testadas:

    
n=(int(input("Digite um número inteiro positivo: "))) + 1
ciclo = 1
marcador = 1
while marcador < n:
    print(ciclo)
    ciclo = ciclo+2
    marcador = marcador + 1
    

n=(int(input("Digite um número inteiro positivo: "))) + 1
ciclo = 1
marcador = 2
while marcador <= n:
     print(ciclo)
     ciclo = ciclo+2
     marcador = marcador + 1
        
"""