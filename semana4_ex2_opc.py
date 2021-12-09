# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 15:14:41 2021

Escreva um programa que receba um número inteiro na entrada e verifique se o
número recebido possui ao menos um dígito com um dígito adjacente igual a ele.
Caso exista, imprima "sim"; se não existir, imprima "não".

@author: Raphael Aguiar
"""

n = (input("Digite um número inteiro: "))
count = len(n)-1
n = int(n)
resultado = False
while count > 0:
    resto = n % 10
    divisão_inteira = n // 10
    resto2 = divisão_inteira % 10
    if resto2 == resto:
        resultado = True
        break
    else:
        count = count - 1
        n = divisão_inteira
if resultado == False:
    print("não")
else:
    print("sim")      


"""

3456  count=3

    resto = 3456 % 10 = 6
    divisão_inteira = 3456 // 10 = 345
    resto2 = 345 % 10  == 5
    
    resto2 == resto?  5 == 6?
    False

345 count=2

    resto - 345 % 10 = 5
    divisão_inteira = 


    
3456

1 - 345   6
2- 34     5
3- 3      4

34557

1- 3455 7
2- 345  5
3- 34   5
4 3     4
    

"""




