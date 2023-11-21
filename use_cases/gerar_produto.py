cod_atual = 0
def criarProduto(nome, categoria, preco) -> dict:
    global cod_atual
    cod_atual +=1
    produto = {
        'codigo': cod_atual,
        'categoria': categoria,
        'nome': nome,
        'preco': preco
    }
    return produto
