# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 09:45:48 2021

exercício 2 - primos

escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função

exemplos de execução no shell do python:
    
>>> maior_primo(100)
97
>>> maior_primo(7)
7

Dica: escreva uma função éPrimo(k) e faça um laço percorrendo os números até o número dado checando se o número é primo ou não; se for, guarde numa variável.
Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.

@author: Raphael Aguiar
"""

def maior_primo(x):
    
    def éPrimo(k):
        contador = resto = 2
        primo = True
    
        while contador < k:
            resto = k % contador
            contador = contador + 1
            if resto == 0:
                primo = False                
        
        if primo:
                return True
        else:
                return False
    
    if x <= 1: 
        return print("O Número deve ser inteiro, positivo e maior que 1.")
    
    else:
        contador = 1
        resultado = 2
    
        while contador <= x:  
            if éPrimo(contador) == True:
                resultado = contador
            contador = contador + 1
        
        return resultado
        
    


