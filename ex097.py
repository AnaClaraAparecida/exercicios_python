from time import sleep
def contador(i, f, p):
    """
    :param i: inicio
    :param f: fim
    :param p:passo
    :return:
    """
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        sleep(2.5)
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!')
#main
contador(1,10,1)
print('~'*30)
contador(10, 0, 2)
print('Agora é a sua vez de iniciar uma contagem:')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
