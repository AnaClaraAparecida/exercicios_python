aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))
print(f'-> O aluno, {aluno["nome"]}')
print(f'-> Teve sua média de, {aluno["média"]}')
if aluno['média'] >= 7:
    print(f'-> E sua situaçao é, APROVADO!')
elif aluno['média'] < 7:
    print(f'-> E sua situaçao é, RECUPERAÇAO!')
else:
    print(f'-> E sua situaçao é, REPROVADO!')