from use_cases.buscar_por_codigo import buscarCodigo
from repositorio import banco

def deletarProduto (codigo: int) -> None:
    produto = buscarCodigo(codigo)
    if produto:
        banco.remove(produto)
        print('Produto removido.')
    else:
        print('Produto não encontrado!')

