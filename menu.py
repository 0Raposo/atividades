from use_cases.adicionar import adicionarProduto
from use_cases.listar import listarProdutos
from use_cases.editar import editarProduto
from use_cases.deletar import deletarProduto


def menu():

        print('---MENU EM PYTHON---')
        print('1 - Cadastrar produto')
        print('2 - Editar produto')
        print('3 - Deletar produto')
        print('4 - Listar todos os produtos')
        print('5 - Sair')
        opcao = int(input('Digite uma opção: '))

        if opcao == 1:
            nome = input('Digite o nome do produto: ')
            categoria = input('Digite a categoria do produto: ')
            preco = input('Digite o preço do produto: ')
            adicionarProduto(nome, categoria, preco)
            menu()

        elif opcao == 2:
            codigo = int(input('Digite o código do produto: '))
            nome = input('Digite o nome do produto: ')
            categoria = input('Digite a categoria do produto: ')
            preco = input('Digite o preço do produto: ')
            editarProduto(codigo, nome, categoria, preco)
            menu()

        elif opcao == 3:
            codigo = int(input('Digite o código do produto: '))
            deletarProduto(codigo)
            menu()

        elif opcao == 4:
            listarProdutos()
            menu()

        elif opcao == 5:
            print('Programa encerrado.')

menu()