numero = 7
contador = 0

while contador < 3:

    resposta = int(input('Bem vindo ao jogo do milhao! Advinhe um numero de 1 a 10 para ganhar 1 kwanza angolano!\n'))
    
    if resposta == numero:
        print('Voce acertou! Parabens!')
        print('Voce ganhou 1 kwanza angolano.')
        break

    else:
        print('Voce errou! Tente novamente.')
        contador += 1

if contador >= 3:
    print('Voce perdeu! O numero era 7!')

