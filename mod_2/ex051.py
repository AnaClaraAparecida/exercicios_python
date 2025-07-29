num = int(input('Digite um numero: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        total += 1
    else:
        print('\033[35m', end='')
    print('{} '.format(c), end='')
print('\n\033[m7O numero {} foi divisivel {} vezes'.format(num, total))
if total == 2:
    print('POR TAL MOTIVO, ELE É PRIMO')
else:
    print('POR TAL MOTIVO ELE NÃO É PRIMO')