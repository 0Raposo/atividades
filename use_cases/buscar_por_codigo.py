from repositorio import banco


def buscarCodigo (codigo: int) -> dict or None:
    for produto in banco:
        if produto['codigo'] == codigo:
            return produto

    return None

