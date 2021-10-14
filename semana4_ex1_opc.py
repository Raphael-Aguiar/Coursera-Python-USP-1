# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 13:15:33 2021


Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. 
Se o número for primo, imprima "primo". 
Caso contrário, imprima "não primo".

@author: Raphael Aguiar
"""

n=(int(input("Digite um número inteiro positivo: ")))
numero_valido = True
if n <= 0:
    print("o Número deve ser inteiro e positivo")
    numero_valido = False
elif n > 0 and  n < 12:
        if n == 2 or n == 3 or n == 5 or n == 7 or n == 11:
            primo = True
        else:
            primo=False   
elif n >= 12:  
    if n % 2 == 0 and n % 3 == 0 and n % 5 == 0 and n % 7 == 0 and n % 11 == 0:
        primo = False
    else:
        primo = True
if primo == True and numero_valido == True:
    print("primo")
elif primo == False and numero_valido == True:
    print("não primo")
else:
    print("Tente outra vez")