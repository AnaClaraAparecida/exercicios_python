print('GERADOR DE PA')
print('-=-' * 10)
primeiro = int(input('primeiro numero: '))
razão = int(input('Razão de PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} - '.format(termo), end=' ')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('quantos termos quer mostsrar a mais: '))
print('Progressaso finalizada com {} termos'.format(total))