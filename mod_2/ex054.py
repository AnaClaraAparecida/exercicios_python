menor = 0
maior = 0
for p in range(1, 6):
    peso = float(input('Qual o peso da pessoa {}: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('a pessoa com o maior peso é {}'.format(maior))
print('a pessoa com o menor peso é {}'.format(menor))

