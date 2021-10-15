#
largura = int(input("Digite a largura :"))
altura = int(input("Digite a altura :"))
l1 = 1
a1 = 1
while a1 <= altura:
    while l1 <= largura:
        print("#", end="")
        l1 = l1 + 1
    print()
    a1 = a1 + 1
    l1 = 1
