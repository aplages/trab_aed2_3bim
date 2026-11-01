""" Selection Sort Recursivo """
def encontra_menor_indice(lista: list, indice: int, fim: int):
    if indice == fim:
        return indice

    indice_menor_resto: int = encontra_menor_indice(lista, indice+1, fim)

    if lista[indice] < lista[indice_menor_resto]:
        return indice
    else:
        return indice_menor_resto


def selection_sort_recursivo(lista: list, inicio: int=0, fim: int = 0):
    """
        Ordena os dados de uma lista usando Selection Sort Recursivo\n
        Retorna a lista ordenada
    """
    if fim == 0:
        fim = len(lista)-1

    if inicio >= fim:
        return lista

    indice_menor = encontra_menor_indice(lista, inicio, fim) # Encontra o menor elemento no resto da lista

    if indice_menor != inicio:
        lista[inicio], lista[indice_menor] = lista[indice_menor], lista[inicio]

    return selection_sort_recursivo(lista, inicio+1, fim)
