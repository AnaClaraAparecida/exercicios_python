pessoas = {}
galera = []
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        else:
            print('ERRO! Digite [M/F]: ')
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite [S/N]: ')
    if resp == 'N':
        break
print(f'a) Ao todo, foram cadastradas {len(galera)} pessoas')
media = soma / len(galera)
print(f'b) A media de idade do grupo é {media:5.2f}')
print('c) As mulheres cadrastradas foram ', end='')
for p in galera:
    if p["nome"] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print(f'd) As pessoas que estao a cima da media são: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')