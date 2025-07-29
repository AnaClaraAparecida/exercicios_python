from random import randint
v = 0
while True:
    gamer = int(input('Digite um numero: '))
    cpu = randint(0, 10)
    total = gamer + cpu
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Escolha par ou impar [P/I]: ')).strip().upper()[0]
    print(f'Sua escolha foi {gamer} e a escolha do seu oponete foi {cpu}, o total foi {total}')
    print('Deu par' if total %2 == 0 else 'Deu impar')
    if tipo == 'P':
        if total %2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU')
            break
    elif tipo == 'I':
        if total %2 == 1:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
        print('Vamos jogar novamente...')
print(f'GAME OVER! Você ganhou {v} vezes!')
