time = []
jogador = {}
part = []
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    totpart = int(input(f'Quantas partidas o {jogador["Nome"]} jogou?: '))
    part.clear()
    for c in range(1, totpart + 1):
        part.append(int(input(f'Quantos gols foram feitos na {c} partida: ')))
    jogador['Gols'] = part[:]
    jogador['Total'] = sum(part)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite [S/N]: ')
    if resp == 'N':
        break
print('-=' * 25)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' *60)
while True:
    busca = int(input('Deseja buscar o codigo de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe um jogador com o codigo {busca}')
    else:
        print(f' -> LEVANTAMENTO DO JOGADOR: {time[busca]["Nome"]} <- ')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'   No jogo {i}, {time[busca]["Nome"]} fez {g} gols')
        print('-' * 60)
print('               --> VOLTE SEMPRE! <--')


