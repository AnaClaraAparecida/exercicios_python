from random import shuffle
n1 = (input('nome do primeiro aluno: '))
n2 = (input('nome do segundo aluno: '))
n3 = (input('nome do terceiro aluno: '))
n4 = (input('nome do quarto aluno: '))
list = [n1, n2, n3, n4]
shuffle(list)
print('a ordem selecionado foi {}'.format(list))