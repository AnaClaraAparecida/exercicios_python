p1 = [[], []]
for n in range(0,7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        p1[0].append(num)
    else:
        p1[1].append(num)
print(f'Os numerps pares digitados foram: {sorted(p1[0])}')
print(f'Os numeros impares digitados foram: {sorted(p1[1])}')