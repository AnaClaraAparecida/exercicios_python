from random import randint
itens = ('Pedra','Papel','Tesoura')
cpu = randint (0,2)
print('''SUAS OPÇOES
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
gamer = int(input('Qual a sua escolha? '))
print('-=-' * 10)
print('Escolha do computador {}'.format(itens [cpu]))
print('Escolha do jogador {}'.format(itens [gamer]))
print('-=-' * 10)
if cpu == 0:
    if gamer == 0:
        print('EMPATE!')
    elif gamer == 1:
        print('VOCÊ VENCEU!')
    elif gamer == 2:
        print('VOCÊ PERDEU!')
elif cpu == 1:
    if gamer == 0:
        print('VOCÊ PERDEU!')
    elif gamer == 1:
        print('EMPATE!')
    elif cpu == 2:
        print('VOCÊ GANHOU!')
elif cpu == 2:
    if gamer == 0:
        print('VOCÊ GANHOU!')
    elif gamer == 1:
        print('VOCÊ PERDEU!')
    elif gamer == 2:
        print('EMPATE!')



