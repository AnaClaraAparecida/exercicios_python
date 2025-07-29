n = (int(input('Digite um valor: ')), int(input('Digite um valor: ')),
    int(input('Digite um valor: ')), int(input('Digite um valor: ')))
print(f'Os valores digitados foram {n}')
print(f'O numero 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O numero 3 apareceu na posiçao {n.index(3)+1}')
else:
    print('O valor 3 não foi digitado')
print('OS numeros pares digitados foram: ', end='{ ')
for num in n:
    if num % 2 == 0:
        print(num, end=', ')

