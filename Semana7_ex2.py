#
largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
l1 = 1
a1 = 1

# Primeira linha do retângulo:
while l1 <= largura:
        print("#", end="")
        l1 = l1 + 1
print()

# Demais linhas do retângulo exceto linha final:
l1 = 1
a1 = a1 + 1
while a1 < altura:
    print("#", end="")
    while l1 < largura - 1:
        print(" ", end="")
        l1 = l1 + 1
    print("#")
    a1 = a1 + 1
    l1 = 1

# Linha final retângulo:
while l1 <= largura:
        print("#", end="")
        l1 = l1 + 1
print()