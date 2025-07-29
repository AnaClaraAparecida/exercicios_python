list = []
maior = 0
menor = 0
for c in range(0, 5):
    list.append(int(input(f'Digite um numero para a posição {c}: ')))
    if c == 0:
        maior = menor = list[c]
    else:
        if list[c] > maior:
            maior = list[c]
        if list[c] < menor:
            menor =  list[c]
print(f'Os numeros digitados foram {list}')
print(f'O maior numero digitado foi {maior}, nas posições: ', end= ' ')
for a, b in enumerate(list):
    if b == maior:
        print(f'{a}...', end= ' ')
print(f'\nO menor numero digitado foi {menor}, nas posições: ', end= ' ')
for a, b  in enumerate(list):
    if b == menor:
        print(f'{a}...', end= ' ')
