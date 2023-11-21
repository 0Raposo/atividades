from use_cases.buscar_por_codigo import buscarCodigo

def editarProduto(codigo, nome, categoria, preco):
    produto = buscarCodigo(codigo)
    if produto:
            produto['nome']= nome,
            produto['categoria']= categoria,
            produto['preco']= preco

    else:
        print('Produto não encontrado.')

