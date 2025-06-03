from listaencad import ListaEncadeada

def main():
    l1 = ListaEncadeada()
    l2 = ListaEncadeada()

    for v in [1, 3, 5, 7]:
        l1.inserir_fim(v)
    for v in [2, 4, 6, 8]:
        l2.inserir_fim(v)

    print("Lista 1:")
    l1.exibir()
    print("Lista 2:")
    l2.exibir()

    print("\nMesclando listas ordenadas:")
    l1.mesclar_listas(l2, ordenada=True)
    print("Lista mesclada:")
    l1.exibir()

    for v in [9, 10]:
        l2.inserir_fim(v)

    print("\nComparando com nova lista 2:")
    print("São iguais?", l1.comparar_listas(l2))

    print("\nRemovendo todas as ocorrências de 5:")
    l1.remover_todas_ocorrencias(5)
    l1.exibir()

if __name__ == "__main__":
    main()
