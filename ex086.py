p = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somaC = maior = 0
for l in range(0,3):
    for c in range(0, 3):
        p[l][c] = int(input('digite um valor: '))
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{p[l][c]}]', end=' ')
    print()
for l in range(0,3):
    for c in range(0,3):
        if p[l][c] % 2 == 0:
           soma += p[l][c]
for l in range(0,3):
    somaC += p[l][2]
for c in range(0,3):
    for c in range(3):
        if l == 1:
            if p[l][c] > maior:
                maior = p[l][c]
print(f'As soma dos numeros pares é: {soma}')
print(f'A soma dos valores da terceira coluna são: {somaC}')
print(f'O maior valor da segunda linha é: {maior}')
