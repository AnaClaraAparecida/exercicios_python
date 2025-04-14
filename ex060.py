print('GERADOR DE PA')
print('-=-' * 10)
primeiro = int(input('primeiro numero: '))
razão = int(input('Razão de PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end=' ')
    termo += razão
    cont += 1
print('FIM ')