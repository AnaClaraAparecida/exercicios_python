larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('sua parede tem a dimensao {}x{} e a sua area é igual a {}'.format(larg, alt, area))
tinta = area / 2
print('para pintar esta parede, serão necassarias de {}L de tinta'.format(tinta))
