from random import randint
n = (randint(1,10), randint(1,10), randint(1,10),
     randint(1,10), randint(1,10), )
print(f'Os numeros sorteados foram {n}')
print(f'O maior numero foi {max(n)}')
print(f'O menor numero foi {min(n)}')