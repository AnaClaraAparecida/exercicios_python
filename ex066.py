
while True:
    n = int(input('Digite um numero para ver sua tabuada correspondente: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
print('PROGRAM ENCERRADO... VOLTE SEMPRE')




