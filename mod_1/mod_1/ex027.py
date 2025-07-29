from random import randint
from time import sleep
cpu = randint(0, 5)
print('-=-'* 20)
print('Vou pensar em um numero de 0 a 5. Tente adivinhar...')
print('-=-'* 20)
n = int(input('Que numero eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if n == cpu:
    print(' WINNER, você conseguiu acertar!'.format(n))
else:
    print('LOSER, eu pensei no {} e não no {}'.format(cpu, n))

