lista = []
for c in range(0, 5):
    num = int(input('Digite um numero: '))
    if c == 0 or num > lista [-1]:
        lista.append(num)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionada na posição {pos} na lista')
                break
            pos += 1
print('-=-' * 20)
print(f'Os numeros digitados em ordem são: {lista}')




