from repositorio import banco
from use_cases.adicionar import adicionarProduto
def listarProdutos():
    print('---LISTA DE PRODUTOS---')
    if banco:
        for produto in banco:
            print(f'Código: {produto["codigo"]}')
            print(f'Nome: {produto["nome"]}')
            print(f'Categoria: {produto["categoria"]}')
            print(f'Preço: {produto["preco"]}')
            print('-'*50)
    else:
        print('Banco vazio!')
