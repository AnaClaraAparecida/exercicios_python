from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'curso.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opçao de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Sair do sistema
        cabeçalho('Saindo do sistema... Ate logo!')
        break
    else:
        # Digitou uma opçaoç errada no menu
        print('\033[31mERRO, Digite uma opçaçao valida\033[m')
    sleep(2)

