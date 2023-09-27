from palavraforca import palavra
import random
import sys
import os

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    os.system('clear')

palavra = random.choice(palavra)
letras_usuario = []
chances = 5
ganhou = False

print('=#' * 25)
print('=#' * 9 + ' JOGO DA FORCA ' + '=#' * 9)
print('=#' * 25)
print(' ')

while True:
    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print(f' - você tem {chances} chances. DICA: CIDADE BRASILEIRA')
    print(' ')
    print(f'Letras chutadas: {letras_usuario}')
    print(' ')
    tentativa = input('escolha uma letra: ')
    letras_usuario.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances = chances - 1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f'Parabéns, você ganhou! A palavra era: {palavra}')
    res = int(input('''Deseja Reiniciar o jogo?
    [ 1 ] = SIM
    [ 2 ] = NÂO
    SUA RESPOSTA: '''))
    if res == 1:
        restart_program()
    if res == 2:
        exit()

else:
    print(f'Você perdeu! A palavra era: {palavra}')
    res = int(input('''Deseja Reiniciar o jogo?
        [ 1 ] = SIM
        [ 2 ] = NÂO
        SUA RESPOSTA: j
        '''))
    if res == 1:
        restart_program()
    if res == 2:
        exit()







