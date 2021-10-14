


def computador_escolhe_jogada(n,m):
    # recebe, como parâmetros, os números n e m descritos acima e devolve um inteiro correspondente à próxima jogada do computador 
    # (ou seja, quantas peças o computador deve retirar do tabuleiro) de acordo com a estratégia vencedora.
    if n > m:
        jogada = 1
        while (n - jogada) % (m + 1) != 0:
            jogada = jogada + 1
        if jogada < m:
            return jogada
        else:
            return m
    else:
        return m   


def usuario_escolhe_jogada(n,m):
    # recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e verifica se o valor informado é válido. 
    # Se o valor informado for válido, a função deve devolvê-lo; caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.
    jogada = input("Quantas peças você vai tirar? ")
    jogada = int(jogada)
    if jogada > m:
        while jogada > m:
            jogada = input("Oops! Jogada inválida! Tente de novo ")
            jogada = int(jogada)
            return jogada
    else:
        return jogada


print(computador_escolhe_jogada(30,3))

