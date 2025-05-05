list = ('blusas', 19.99,
        'jaquetas', 59.99,
        'calças jeans', 49.99,
        'shorts jeans', 39.99,
        'leggins', 19.99,
        'conjuntos', 49.99)
print('-~' * 20)
print(f'{"TABELA DE PREÇOS": ^30}')
print('~-' * 20)
for p in range(0, len(list)):
    if p %2 == 0:
        print(f'{list[p]:.<20}', end= '')
    else:
        print(f'R${list[p]:>7}')
print('-~' * 20)