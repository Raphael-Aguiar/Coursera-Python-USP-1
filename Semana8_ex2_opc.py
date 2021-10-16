# Exercício 2 - Invertendo sequência
# Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números inteiros e imprima todos os valores em ordem inversa. 
# A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.

n = 1
lista = []
while n != 0:
    n = int(input("Digite um número inteiro: "))
    lista.append(n)
del lista[-1]
lista_inversa = []
tamanho = - len(lista)
x = -1
while x >= (tamanho):
    lista_inversa.append(lista[x])
    x = x - 1
for i in lista_inversa:
    print(i)