print('-=-' * 9)
print('Analisador de triangulos: ')
print('-=-' * 9)
r1 = float(input('primeira reta: '))
r2 = float(input('segunda reta: '))
r3 = float(input('terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 < r2:
    print('As retas a cima PODEM formar TRIANGULOS! ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('As retas a cima NÃO podem formar TRIANGULOS! ')