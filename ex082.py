lista = []
exp = str(input('Digite uma expressão: '))
for simb in exp:
    if simb in '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão esta valida! ')
else:
    print('Sua expressão esta invalida')