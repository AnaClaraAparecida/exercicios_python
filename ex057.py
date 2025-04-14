from operator import truediv
from random import randint
cpu = randint(0, 10)
print('Ola, eu sou o compurtador, e estou pensando em um numero de 0 a 10!')
print('Você consegue adivinhar o numero que eu escolhi?')
acerto = 0
palpites = 0
while not acerto:
     gamer = int(input('Qual o seu palpite? '))
     palpites += 1
     if gamer == cpu:
         acerto = True
     else:
         if gamer < cpu:
             print('Maior... Tente novamente! ')
         elif gamer > cpu:
             print('Menor... Tente novamente! ')
print('Acertou em {} tentativas, PARABENS! '.format(palpites))
