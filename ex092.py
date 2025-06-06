jogador = {}
part = []
jogador['Nome'] = str(input('Nome do jogador: '))
totpart = int(input(f'Quantas partidas o {jogador["Nome"]} jogou?: '))
for c in range(1, totpart + 1):
    part.append(int(input(f'Quantos gols foram feitos na {c} partida: ')))
jogador['Gols'] = part[:]
jogador['Total'] = sum(part)
print('_-' *30)
print(jogador)
print('_-' *30)
for k, v in jogador.items():
    print(f'No campo {k}, foi preenchido {v}')
print('_-' *30)
print(f'O jogadro {jogador["Nome"]} teve no total {totpart} partidas')
for k, v in enumerate(jogador['Gols']):
    print(f'    -> Na partida {k + 1        }, fez {v} gols')
print(f'No total, o {jogador["Nome"]} fez {jogador["Total"]} gols')
