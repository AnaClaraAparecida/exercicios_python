tot18 = totM = totF = 0
while True:
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo: [F/M]: ')).strip().upper()[0]
    idade = int(input('idade: '))
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totM += 1
    if sexo == 'F' and idade < 20:
        totF += 1
    resp = (' ')
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18: {tot18}')
print(f'Total de homens cadastrados: {totM}')
print(f'Total de mulheres com menos de vinte anos: {totF}')
