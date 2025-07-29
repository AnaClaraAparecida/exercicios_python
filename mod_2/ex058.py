n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
opção = 0
while opção != 5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa''')
    opção = int(input('Qual a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O produto entre {} e {} é igual {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('O maior numero de {} e {} é {}'. format(n1, n2, maior))
    elif opção == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite um numero: '))
    elif opção == 5:
        print('finalizando...')
    else:
        print('Opção invalida, tente novamente! ')
    print('=-=' * 10)
print('Fim do programa, volte sempre!')
