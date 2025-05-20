lista = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2], media])
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'Ss':
        print('ARMAZENADO...')
    elif resp in 'Nn':
        break
    else:
        print('Resposta invalida, tente novamente...')
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-=' * 20)
while True:
    opc = int(input('Mostrar notas de qual aluno? [999 para parar]: '))
    if opc == 999:
         print('FINALIZANDO...')
         break
    if opc <= len(lista) - 1:
        print(f'As notas de {lista[opc][0]} são {lista[opc][1]}')
print('<<<< VOLTE SEMPRE >>>>')


