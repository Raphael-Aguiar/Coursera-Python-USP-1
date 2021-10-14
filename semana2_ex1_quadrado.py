# Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.
# Observação: a saída deve estar no formato: "perímetro: x - área: y"

lado_quadrado=input("Digite o valor do lado do quadrado em metros: ")
lado_quadrado=int(lado_quadrado)
print("perímetro:", lado_quadrado * 4, "- área:", lado_quadrado ** 2)