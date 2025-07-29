list = []
while True:
    num = int(input('Digite um numero: '))
    if num not in list:
        list.append(num)
        print('Numero adicionado com sucesso...')
    else:
        print('Numero já existente, falha ao adicionar...')
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-=-' * 15)
list.sort()
print(f'Os numero digitados foram: {list}')

