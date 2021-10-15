

# Programa que pede ao usuário para digitar um número qualquer e o fatora enquanto o usuário não digitar zero
def fatorial(x):
    fatorial = x - 1
    while fatorial > 1:
        x = x * fatorial
        fatorial = fatorial - 1
    return x
x = 2
while x > 0:
    x = int(input("Digite um número inteiro positivo: "))
    y = fatorial(x)
    print(y)
    
# Código sem a função "fatorial" acima:  
'''
x = 2
while x > 1:
    x = int(input("Digite um número inteiro positivo: "))
    fatorial = x-1
    while fatorial > 1:
        x = x * fatorial
        fatorial = fatorial - 1
    print(x)
'''



