from random import randint
from time import sleep
def sorteia(listanum):
    """
    :param listanum:
    :return:
    """
    print('Sorteando 5 valores da lista: ', end=' ')
    for cont in range(0, 5):
        n = randint(1, 10)
        listanum.append(n)
        print(f'{n} ',end=' ' )
        sleep(0.4)
def somapar(listanum):
    soma = 0
    for v in listanum:
        if v % 2 == 0:
            soma += v
    for p in listanum:
        if p % 2 == 0:
            resp = p
            print(f'\nValor par: {p}', end='')
    print(f'\nSomando os valores pares de {listanum}, temos {soma}')


num = []
#mean
sorteia(num)
somapar(num)

