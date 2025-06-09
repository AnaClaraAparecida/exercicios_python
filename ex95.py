def area(l, c):
    a = l * c
    print(f'A area de um terreno com extensao de {l}x{c} é {a}m')
#principal
print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (c): '))
area (l,c)