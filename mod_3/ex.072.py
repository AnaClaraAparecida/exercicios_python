times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Bragantino', 'Ceará',
         'Corinthians', 'Cruzeiro', 'Vasco', 'Juventude', 'São Paulo',
         'Mirassol', 'Internacional', 'Bahia', 'Fortaleza', 'Botafogo',
         'Vitória', 'Atlético-MG', 'Santos', 'Grêmio', 'Sport')
print('-=' * 20)
print(f'O vinte primeiros times são: {times}')
print('-=' * 20)
print(f'Os cinco primeiros colocados são: {times[:5]}')
print('-=' * 20)
print(f'Os ultimos quatro colocados são: {times[16:]}')
print('-=' * 20)
print(f'Os times em ordem alfabetica são: {sorted(times)}')
print('-=' * 20)
print(f'O Gremio esta na classificação: {times.index("Grêmio")+1}')
print('-=' * 20)


