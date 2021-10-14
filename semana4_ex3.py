# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 12:22:01 2021

Exercício 3
  Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

Exemplo:

Digite um número inteiro: 123
6

Dica: Para separar os dígitos, lembre-se: o operador "//" faz uma divisão inteira jogando fora o resto, ou seja, aquilo que é menor que o divisor; O operador "%" devolve 
apenas o resto da divisão inteira jogando fora o resultado, ou seja, tudo que é maior ou igual ao divisor.

@author: Raphael Aguiar
"""

n=(int(input("Digite um número inteiro positivo: ")))
divisão_inteira = 10
resto = 0
while divisão_inteira >= 10:
    resto = resto + (n % 10)
    divisão_inteira = n // 10
    n = divisão_inteira
resto = resto + n
print(resto)



"""

541 - resto 1    divisão = 54
54  - resto 4    divisão 5

"""





 
