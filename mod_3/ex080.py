lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp in 'Ss':
        print('Armazenado...')
    elif resp in 'Nn':
        print('Programa finalizado')
        break
    else:
        print('Resposta invalida')
print('-=-'* 15)
if 5 in lista:
    print('O valor 5, esta na lista!')
else:
    print('O valor 5, não faz parte da lista!')
print(f'foram digitados {len(lista)} numeros: {lista}')
lista.sort(reverse=True)
print(f'em sua forma decrescente: {lista}')
