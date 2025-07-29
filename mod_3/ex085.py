p = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0, 3):
        p[l][c] = int(input(f'digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{p[l][c]}]', end=' ')
    print()
