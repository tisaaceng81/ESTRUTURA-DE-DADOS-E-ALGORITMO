# main.py
import sys
from cABB import cABB, percursos, tiposNo



def executar(argv):
    arvore = cABB()

    if len(argv) == 1:
        print("Modo padrão: executando árvore de exemplo...")
        for v in [50, 30, 70, 20, 40, 60, 80]:
            arvore.inserir(v)

        print("\nÁrvore In-Ordem:")
        arvore.percorreArvore(percursos.IN_ORDEM)
        print("\nVisualização da estrutura da árvore:")
        arvore.imprimirArvore()
        return

    comando = argv[1].lower()

    if comando == "inserir":
        for valor in map(int, argv[2:]):
            arvore.inserir(valor)
        print("Valores inseridos com sucesso.")
        arvore.imprimirArvore()

    elif comando == "remover":
        for valor in map(int, argv[2:]):
            ok = arvore.remover(valor)
            print(f"Remover {valor}: {'Sucesso' if ok else 'Não encontrado'}")
        arvore.imprimirArvore()

    elif comando == "buscar":
        if len(argv) < 3:
            print("Uso: buscar <valor>")
        else:
            valor = int(argv[2])
            encontrado = arvore.buscar(valor)
            print(f"Buscar {valor}: {'Encontrado' if encontrado else 'Não encontrado'}")

    elif comando == "imprimir":
        print("Imprimindo árvore:")
        arvore.imprimirArvore()

    elif comando == "espelhar":
        arvore.espelhar()
        print("Árvore espelhada:")
        arvore.imprimirArvore()

    elif comando == "altura":
        print("Altura da árvore:", arvore.altura())

    elif comando == "contar_total":
        print("Total de nós:", arvore.contarNosTotal())

    elif comando == "contar_tipo":
        if len(argv) < 3:
            print("Uso: contar_tipo <folha|completo|semi>")
        else:
            tipo = argv[2].lower()
            if tipo == "folha":
                print("Nº de folhas:", arvore.contarNos(tiposNo.FOLHA))
            elif tipo == "completo":
                print("Nº de nós completos:", arvore.contarNos(tiposNo.COMPLETO))
            elif tipo == "semi":
                print("Nº de nós semi-cheios:", arvore.contarNos(tiposNo.SEMI_CHEIO))
            else:
                print("Tipo inválido. Use: folha, completo ou semi.")

    elif comando == "exemplo_identicidade":
        arvore1 = cABB()
        arvore2 = cABB()
        for v in [10, 5, 15]:
            arvore1.inserir(v)
            arvore2.inserir(v)
        print("Estruturalmente iguais?", arvore1.estruturalmenteIgual(arvore2))
        print("Idênticas?", arvore1.identica(arvore2))
        arvore2.remover(5)
        print("Após remover 5 da segunda:")
        print("Estruturalmente iguais?", arvore1.estruturalmenteIgual(arvore2))
        print("Idênticas?", arvore1.identica(arvore2))

    else:
        print(f"Comando desconhecido: '{comando}'")

if __name__ == '__main__':
    executar(sys.argv)
