
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA!')
    elif 16 >= idade < 18 or idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL!')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATORIO!')
#mean
nasc = int(input('Qual o ano da sua data de nascimento?: '))
print(voto(nasc))

