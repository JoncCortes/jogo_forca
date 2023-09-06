from palavraforca import palavra
from palavraforca import dica

letras_usuario = []
chances = 6
ganhou = False

while True:
    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print(f' - você tem {chances} chances. DICA: {dica}')
    tentativa = input('escolha uma letra: ')
    letras_usuario.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances = chances -1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f'Parabéns, você ganhou! A palavra era: {palavra}')

else:
    print(f'Você perdeu! A palavra era: {palavra}')
