from time import sleep
def maior(* num):
    cont= maior = 0
    print('\nAnalisando os valores passados...')
    for n in num:
        print(f'{n}', end=' ')
        sleep(0.4
              )
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'Forma informados {cont} numeros ao todo')
    print(f'O maior valor, dentre os anteriores, é o  {maior}')
#mean
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()