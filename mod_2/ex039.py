n1 = float(input('Nota de Matematica: '))
n2 = float(input('Nota de Quimica: '))
media = (n1 + n2) / 2
print('Sendo a nota de Matematica {}, e de Quimica {}, sua media é {:.1f}'.format(n1, n2, media))
if media < 5:
    print('\033[31mREPROVADO\033[m')
elif media >= 7:
    print('\033[32mAPROVADO\033[m')
else:
    print('\033[33mRECUPERAÇÃO\033[m')
