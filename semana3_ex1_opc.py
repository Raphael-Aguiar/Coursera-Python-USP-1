# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:57:42 2021

Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. 
Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.
Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima
longe
na saída. 
Caso o contrário, quando a distância for menor que 10, imprima
perto

@author: Raphael Aguiar
"""

x1=int(input("Digite a coordenada X do primeiro número: "))
y1=int(input("Digite a coordenada y do primeiro número: "))
x2=int(input("Digite a coordenada X do segundo número: "))
y2=int(input("Digite a coordenada y do segundo número: "))

import math
d=math.sqrt(((x1-x2)**2)+((y1-y2)**2))

if d >= 10:
    print("longe")
else:
    print("perto")
    