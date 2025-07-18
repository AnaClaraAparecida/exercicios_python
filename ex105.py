from time import sleep
c = ['\033[m',        #0 -> sem cor
     '\033[0;30;41m', #1 -> vermelho
     '\033[0;30;42m', #2 -> verde
     '\033[0;30;43m', #3 -> amarelo
     '\033[0;30;44m', #4 -> azul
     '\033[0;30;45m', #5 -> roxo
     '\033[7;30m',    #6 -> branco
     ]
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}', 2)
    help(com)
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

#mean
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP',5)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO!',4)