print('Bem-Vindo ao Controle de Funcionários do Isaque')
print('*' * 76)

# lista que armazena os dicionários
funcionarios = []
# contador para definir ID dos funcionários
contador = 57


def cadastro_funcionario(id):
    print('-' * 30, 'MENU CADASTRAR FUNCIONÁRIO', '-' * 30)
    while True:
        try:
            nome = input('Entre com o NOME: ')
            setor = input('Entre com o SETOR: ')
            salario = float(input('Entre com o SALÁRIO: '))
            break
        except ValueError:
            # tratamento de excação para aceitar apenas valores inteiros ou com ponto flutuante
            print('Salário INVÁLIDO')
            print('Tente novamente')
    dicionarioFuncionarios = {'id': id,
                              'nome': nome,
                              'setor': setor,
                              'salario': salario}
    funcionarios.append(dicionarioFuncionarios.copy())


def consultar_funcionario():
    print('-' * 30, 'MENU CONSULTAR FUNCIONÁRIO', '-' * 30)
    while True:
        # Como não foi especificado o tratamento de exceções neste exercício
        # foram usadas STRINGS nas opções, afim de evitar erros no sistema.
        print('Escolha a opção de consulta desejada: ')
        print('1 - Consultar TODOS os Funcionários')
        print('2 - Consultar FUNCIONÁRIO por ID')
        print('3 - Consultar FUNCIONÁRIO(S) por Setor')
        print('4 - Retornar ao menu anterior')
        escolha = input('')

        if escolha == '1':
            # Consultar TODOS os Funcionários
            for dicionarioFuncionarios in funcionarios:
                for key, value in dicionarioFuncionarios.items():
                    print('{} : {}'.format(key, value))


        elif escolha == '2':
            # Consultar funcionário por ID
            entrada = int(input('Insira o ID do Funcionário: '))
            for dicionarioFuncionarios in funcionarios:
                if (dicionarioFuncionarios['id'] == entrada):
                    for key, value in dicionarioFuncionarios.items():
                        print('{} : {}'.format(key, value))


        elif escolha == '3':
            # Consultar funcionário por setor
            entrada = input('Digite o setor do Funcionário: ')
            for dicionarioFuncionarios in funcionarios:
                if dicionarioFuncionarios['setor'] == entrada:
                    for key, value in dicionarioFuncionarios.items():
                        print('{} : {}'.format(key, value))

        elif escolha == '4':
            # retornar ao menu anterior
            return
        else:
            print('Valor inválido, tente novamente')


def remover_funcionario():
    # laço "for" procura na lista por um par de id e entrada,
    # então deleta o dicionario referente a entrada

    print('-' * 30, 'MENU REMOVER FUNCIONÁRIO', '-' * 30)
    entrada = int(input('Digite o código do Funcionário a ser removido: '))
    for dicionarioFuncionarios in funcionarios:
        if dicionarioFuncionarios['id'] == entrada:
            funcionarios.remove(dicionarioFuncionarios)
            print('Funcionário removido com sucesso!')
            return


# Função principal do programa
print('-' * 30, 'MENU PRINCIPAL', '-' * 30)
while True:
    # Como não foi especificado o tratamento de exceções neste exercício
    # foram usadas STRINGS nas opções, afim de evitar erros no sistema.
    print('Escolha a opção desejada: ')
    print('1 - Cadastrar Funcionário')
    print('2 - Consultar Funcionário(s)')
    print('3 - Remover Funcionário')
    print('4 - Sair')
    opcao = input('')
    if opcao == '1':
        contador += 1
        cadastro_funcionario(contador)
    elif opcao == '2':
        consultar_funcionario()
    elif opcao == '3':
        remover_funcionario()
    elif opcao == '4':
        break

print('Finalizando...')
