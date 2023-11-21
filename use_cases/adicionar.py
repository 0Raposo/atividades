from repositorio import banco
from use_cases.gerar_produto import criarProduto

# codigo - nome - categorai - preço
def adicionarProduto (nome,categoria,preco):
    produto = criarProduto(nome,categoria,preco)
    banco.append(produto)
    print('Produto adicionado com sucesso.')


