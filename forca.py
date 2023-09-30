import random
import sys
import os

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def textosIniciais():
    print('=#' * 25)
    print('=#' * 9 + ' JOGO DA FORCA ' + '=#' * 9)
    print('=#' * 25)
    print(' ')
    print(' ### COMO JOGAR ### ')
    print('Digite uma letra para checar se está na palavra')
    print('Caso a letra corresponda, será inserida na palavra')
    print('Caso contrário, perderá uma chance')
    print('* As palavras podem conter acentos e espaços.')
    print(' ')
    print('=#' * 25)
    print('=#' * 5 + ' Criado por JONAS CORTES © 2023 ' + '=#' * 5)
    print('=#' * 25)
    print(' ')
    print(' BOM JOGO! ')
    print('=#' * 36)
    print(' ')


palavra = [
    "casa", "carro", "gato", "cachorro", "futebol", "escola", "amigo", "computador", "trabalho", "cidade",
    "verão", "inverno", "primavera", "outono", "música", "filme", "livro", "jardim", "praia", "montanha",
    "viagem", "restaurante", "café", "família", "amor", "vida", "tempo", "dia", "noite", "lua", "sol",
    "chuva", "arco-íris", "vento", "mar", "rio", "ponte", "caminho", "porta", "janela", "espelho", "relógio",
    "telefone", "fotografia", "arte", "pintura", "escultura", "cor", "azul", "vermelho", "verde", "amarelo",
"laranja", "rosa", "roxo", "branco", "preto", "bola", "bicicleta", "tênis", "sapato", "camisa", "calça",
"chapéu", "óculos", "mochila", "cachecol", "frio", "calor", "alegria", "tristeza", "medo", "surpresa",
    "sonho", "esperança", "sorriso", "riso", "abraço", "beijo", "lágrima", "saúde", "doença", "fome", "sede",
"amizade", "companheiro", "coração", "pensamento", "palavra", "frase", "silêncio", "natureza", "planeta",
    "universo", "ciência", "tecnologia", "felicidade", "desafio", "conquista", "vitória", "derrota", "aprendizado",
]

palavra = random.choice(palavra)
letras_usuario = []
chances = 5
ganhou = False

textosIniciais()


while True:
    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print(f' - você tem {chances} chances. DICA: PALAVRAS EM PORTUGUÊS.')
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
        SUA RESPOSTA: '''))
    if res == 1:
        restart_program()
    if res == 2:
        exit()







