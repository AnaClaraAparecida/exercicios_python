lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um numero: ')))
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resp in 'Ss':
        print('armazenado...')
    elif resp in 'Nn':
        break
    else:
        print('resposta invalida, tente novamente...')
for num in lista:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(f'A lista é: {lista}')
print(f'Os numeros pares são: {par}')
print(f'Os numeros impares são: {impar}')



