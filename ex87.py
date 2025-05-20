from random import randint
from time import sleep
lista = []
jogos = []
print('-=' * 10, '    JOGOS DA MEGA SENA    ', '-=' * 10)
quant = int(input('Digite a quantidade de jogos para sorteio: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('¨' * 20 ,f'    SORTEANDO {quant} JOGOS    ', '¨' * 20)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(2)