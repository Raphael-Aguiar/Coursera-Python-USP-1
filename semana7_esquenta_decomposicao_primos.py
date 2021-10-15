# Retorna a decomposição do número fornecido em números primos

# Resolução mais simples pelo professor do curso:
# Loop interno para ver quantas vezes o n é divisível por 2 ... depois por 3... depois...
# Loop externo para mudar o divisor

n = int(input("Digite um número inteiro positivo: "))

if n < 1:
    print("Número inválido!")

fator = 2
multiplicidade = 0

# Tentando ir além do exercício e printar de forma mais adequada a fatoração (Ex: 2 ^ 2 X 3 ^3 ...)
while n > 1:
    while n % fator == 0:
        multiplicidade = multiplicidade + 1
        n = n / fator
        if fator == 2:
            print(fator, end="")
        else:
            print (" X ", fator)
    if multiplicidade < 2:
            print (" X")            
    else:
        print(" ^",multiplicidade,end="" )
    fator = fator + 1
print("X ", fator)






'''
def é_primo(n):
    count = 2
    while count < n:
        if n % count != 0:
            count = count + 1
        else:
            return False
    return True

def menor_divisor_primo(n):
    divisor = 2
    while divisor < n:
        if é_primo(divisor) == True:
            if n % divisor == 0:
                return divisor
            else:
                divisor = divisor + 1
        else:
            divisor = divisor + 1
    return divisor
    

n = int(input("Digite um número inteiro positivo: "))

if n < 1:
    print("Número inválido!")

mdp = menor_divisor_primo(n)
quociente = n / mdp

if é_primo(quociente) == True:
    print(mdp,"X ", int(quociente))

else:
    
    while é_primo(quociente) == False:
        print(mdp,"X ", end="")
        n = quociente
        mdp = menor_divisor_primo(n)
        quociente = n / mdp
        é_primo(quociente)
    
    print(mdp,"X", int(quociente))
'''