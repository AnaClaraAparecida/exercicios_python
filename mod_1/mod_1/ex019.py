from random import choice
n1 = input('nome do primeiro aluno: ')
n2 = input('nome do segundo aluno: ')
n3 = input('nome do terceiro aluno: ')
n4 = input('nome do quartto aluno: ')
lista = [n1, n2, n3, n4]
escolha = choice(lista)
print('o aluno escolhido foi {}'.format(escolha))