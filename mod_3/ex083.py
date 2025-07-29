p1 = []
p2 = []
cont = maior = menor = 0
while True:
    p1.append(str(input('nome: ')))
    p1.append(float(input('peso: ')))
    cont += 1
    if len(p2) == 0:
        maior = menor = p1[1]
    else:
        if p1[1] > maior:
            maior = p1[1]
        if p1[1] < menor:
            menor = p1[1]
    p2.append(p1[:])
    p1.clear()
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'Ss':
        print('Dado armazenado...')
    elif resp in 'Nn':
        break
    else:
        print('Resposta invalida, tente novamente!')
print(f'Ao total, são: {cont} pessoas')
print(f'o maior peso foi: {maior}Kg, de ', end=' ')
for p in p2:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi: {menor}Kg, de ', end= ' ')
for p in p2:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print()