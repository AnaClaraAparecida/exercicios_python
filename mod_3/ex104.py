def notas(*n, sit=False):
    """
    -> Funçao para analisar notas e situaçoes de varios alunos
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou nao adicionar a situaçao
    :return: dicionario com varias informaçoes sobre a situaçao da turma
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] > 7:
            r['situaçao'] = 'BOA!'
        elif r['media'] >= 5:
            r['situaçao'] = 'RAZOAVEL!'
        else:
            r['situaçao'] = 'RUIM!'
    return r

#meain
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)