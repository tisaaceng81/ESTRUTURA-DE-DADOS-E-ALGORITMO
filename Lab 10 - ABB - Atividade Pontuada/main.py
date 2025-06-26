# Lab10 - Árvore Binária de Busca

import sys
import os
from cABB import cABB, tiposNo

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQ_DADOS = os.path.join(BASE_DIR, "dados.txt")

def carregar_arquivo(arvore):
    if not os.path.exists(ARQ_DADOS):
        return
    with open(ARQ_DADOS, "r") as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                try:
                    arvore.inserir(int(linha))
                except:
                    pass

def salvar_arquivo(arvore):
    with open(ARQ_DADOS, "w") as f:
        def escrever(no):
            if no is None:
                return
            escrever(no._cNo__filhoEsc)
            f.write(str(no.getDado()) + "\n")
            escrever(no._cNo__filhoDir)
        escrever(arvore._cABB__raiz)

def main():
    arvore = cABB()
    if len(sys.argv) > 1:
        comando = sys.argv[1]
        args = sys.argv[2:]

        if comando == "inserir":
            carregar_arquivo(arvore)
            if not args:
                print("Informe valores para inserir.")
                return
            for v in args:
                try:
                    val = int(v)
                except ValueError:
                    print(f"'{v}' não é inteiro válido.")
                    continue
                if arvore.inserir(val):
                    print(f"Valor {val} inserido com sucesso.")
                else:
                    print(f"Valor {val} já existe na árvore.")
            salvar_arquivo(arvore)
            print("\nÁrvore após inserções:")
            arvore.imprimirArvore()

        elif comando == "contar_tipos":
            carregar_arquivo(arvore)
            print("Folhas:     ", arvore.contarNos(tiposNo.FOLHA))
            print("Completos:  ", arvore.contarNos(tiposNo.COMPLETO))
            print("Semi-Cheios:", arvore.contarNos(tiposNo.SEMI_CHEIO))

        elif comando == "buscar":
            carregar_arquivo(arvore)
            if not args:
                print("Informe o valor a buscar.")
                return
            try:
                val = int(args[0])
            except ValueError:
                print("Valor inválido. Use um inteiro.")
                return
            print(f"Busca {val}: {'Encontrado' if arvore.buscar(val) else 'Não encontrado'}")

        elif comando == "remover":
            carregar_arquivo(arvore)
            if not args:
                print("Informe o valor a remover.")
                return
            try:
                val = int(args[0])
            except ValueError:
                print("Valor inválido. Use um inteiro.")
                return
            ok = arvore.remover(val)
            print(f"Remoção de {val}: {'Removido' if ok else 'Não encontrado'}")
            if ok:
                salvar_arquivo(arvore)

        elif comando == "altura":
            carregar_arquivo(arvore)
            print("Altura da árvore:", arvore.altura())

        elif comando == "imprimir":
            carregar_arquivo(arvore)
            print("Estrutura da árvore:")
            arvore.imprimirArvore()

        elif comando == "reset":
            open(ARQ_DADOS, "w").close()
            print("Dados apagados. Árvore reiniciada.")

        elif comando == "estruturalmente_iguais":
            if '--' not in args:
                print("Use o formato: estruturalmente_iguais <valores arv1> -- <valores arv2>")
                return
            separador = args.index('--')
            vals1 = args[:separador]
            vals2 = args[separador+1:]

            arv1 = cABB()
            arv2 = cABB()

            for v in vals1:
                try:
                    arv1.inserir(int(v))
                except:
                    pass

            for v in vals2:
                try:
                    arv2.inserir(int(v))
                except:
                    pass

            print("Árvores estruturalmente iguais?" , "Sim ✅" if arv1.estruturalmenteIgual(arv2) else "Não ❌")

        elif comando == "identicas":
            if '--' not in args:
                print("Use o formato: identicas <valores arv1> -- <valores arv2>")
                return
            separador = args.index('--')
            vals1 = args[:separador]
            vals2 = args[separador+1:]

            arv1 = cABB()
            arv2 = cABB()

            for v in vals1:
                try:
                    arv1.inserir(int(v))
                except:
                    pass

            for v in vals2:
                try:
                    arv2.inserir(int(v))
                except:
                    pass

            print("Árvores idênticas?" , "Sim ✅" if arv1.identica(arv2) else "Não ❌")

        elif comando == "espelhar":
            carregar_arquivo(arvore)
            print("Antes de espelhar:")
            arvore.imprimirArvore()
            print("\nEspelhando...")
            arvore.espelhar()
            print("Após espelhar:")
            arvore.imprimirArvore()
            salvar_arquivo(arvore)

        elif comando == "intervalo":
            carregar_arquivo(arvore)
            if len(args) != 2:
                print("Uso: intervalo <min> <max>")
                return
            try:
                minimo = int(args[0])
                maximo = int(args[1])
            except ValueError:
                print("Valores devem ser inteiros.")
                return
            print(f"Valores no intervalo [{minimo}, {maximo}]:")
            atual = arvore.listarIntervalo(minimo, maximo)
            while atual:
                print(atual.valor, end=" ")
                atual = atual.prox
            print()

        elif comando == "remover_intervalo":
            carregar_arquivo(arvore)
            if len(args) != 2:
                print("Uso: remover_intervalo <min> <max>")
                return
            try:
                minimo = int(args[0])
                maximo = int(args[1])
            except ValueError:
                print("Valores devem ser inteiros.")
                return
            print(f"Removendo valores no intervalo [{minimo}, {maximo}]...")
            arvore.removerIntervalo(minimo, maximo)
            salvar_arquivo(arvore)
            print("Árvore após remoções:")
            arvore.imprimirArvore()

        else:
            print(f"Comando desconhecido: '{comando}'")
        return

    while True:
        print("\nDigite a opção:")
        print("[1] inserir")
        print("[2] contar_tipos")
        print("[3] buscar")
        print("[4] remover")
        print("[5] altura")
        print("[6] imprimir")
        print("[7] reset")
        print("[8] estruturalmente iguais")
        print("[9] idênticas")
        print("[10] espelhar árvore")
        print("[11] listar intervalo [min, max]")
        print("[12] remover intervalo [min, max]")
        print("[0] sair")

        opcao = input("Opção: ").strip()

        if opcao == "1":
            linha = input("Digite valores separados por espaço: ").strip()
            for v in linha.split():
                try:
                    val = int(v)
                except ValueError:
                    print(f"'{v}' não é inteiro válido.")
                    continue
                if arvore.inserir(val):
                    print(f"Valor {val} inserido com sucesso.")
                else:
                    print(f"Valor {val} já existe na árvore.")
            salvar_arquivo(arvore)
            print("\nÁrvore após inserções:")
            arvore.imprimirArvore()

        elif opcao == "2":
            print("Folhas:     ", arvore.contarNos(tiposNo.FOLHA))
            print("Completos:  ", arvore.contarNos(tiposNo.COMPLETO))
            print("Semi-Cheios:", arvore.contarNos(tiposNo.SEMI_CHEIO))

        elif opcao == "3":
            txt = input("Digite o valor para buscar: ").strip()
            try:
                val = int(txt)
            except ValueError:
                print("Valor inválido.")
                continue
            print(f"Busca {val}: {'Encontrado' if arvore.buscar(val) else 'Não encontrado'}")

        elif opcao == "4":
            txt = input("Digite o valor para remover: ").strip()
            try:
                val = int(txt)
            except ValueError:
                print("Valor inválido.")
                continue
            ok = arvore.remover(val)
            print(f"Remoção de {val}: {'Removido' if ok else 'Não encontrado'}")
            if ok:
                salvar_arquivo(arvore)

        elif opcao == "5":
            print("Altura da árvore:", arvore.altura())

        elif opcao == "6":
            print("Estrutura da árvore:")
            arvore.imprimirArvore()

        elif opcao == "7":
            arvore = cABB()
            open(ARQ_DADOS, "w").close()
            print("Árvore reiniciada (memória e arquivo limpos).")

        elif opcao == "8":
            print("Insira os valores da 1ª árvore (separados por espaço):")
            linha1 = input().strip()
            arv1 = cABB()
            for v in linha1.split():
                try:
                    arv1.inserir(int(v))
                except:
                    pass

            print("Insira os valores da 2ª árvore (separados por espaço):")
            linha2 = input().strip()
            arv2 = cABB()
            for v in linha2.split():
                try:
                    arv2.inserir(int(v))
                except:
                    pass

            print("\nEstrutura da 1ª árvore:")
            arv1.imprimirArvore()
            print("\nEstrutura da 2ª árvore:")
            arv2.imprimirArvore()

            print("\nAs árvores são estruturalmente iguais?")
            if arv1.estruturalmenteIgual(arv2):
                print("=> Sim ✅")
            else:
                print("=> Não ❌")

        elif opcao == "9":
            print("Insira os valores da 1ª árvore (separados por espaço):")
            linha1 = input().strip()
            arv1 = cABB()
            for v in linha1.split():
                try:
                    arv1.inserir(int(v))
                except:
                    pass

            print("Insira os valores da 2ª árvore (separados por espaço):")
            linha2 = input().strip()
            arv2 = cABB()
            for v in linha2.split():
                try:
                    arv2.inserir(int(v))
                except:
                    pass

            print("\nEstrutura da 1ª árvore:")
            arv1.imprimirArvore()
            print("\nEstrutura da 2ª árvore:")
            arv2.imprimirArvore()

            print("\nAs árvores são idênticas?")
            if arv1.identica(arv2):
                print("=> Sim ✅")
            else:
                print("=> Não ❌")

        elif opcao == "10":
            print("Antes de espelhar:")
            arvore.imprimirArvore()
            print("\nEspelhando árvore...")
            arvore.espelhar()
            print("Após espelhar:")
            arvore.imprimirArvore()
            salvar_arquivo(arvore)

        elif opcao == "11":
            try:
                minimo = int(input("Informe o valor mínimo: ").strip())
                maximo = int(input("Informe o valor máximo: ").strip())
            except ValueError:
                print("Valores devem ser inteiros.")
                continue
            print(f"Valores no intervalo [{minimo}, {maximo}]:")
            atual = arvore.listarIntervalo(minimo, maximo)
            while atual:
                print(atual.valor, end=" ")
                atual = atual.prox
            print()

        elif opcao == "12":
            try:
                minimo = int(input("Informe o valor mínimo: ").strip())
                maximo = int(input("Informe o valor máximo: ").strip())
            except ValueError:
                print("Valores devem ser inteiros.")
                continue
            print(f"Removendo valores no intervalo [{minimo}, {maximo}]...")
            arvore.removerIntervalo(minimo, maximo)
            salvar_arquivo(arvore)
            print("Árvore após remoções:")
            arvore.imprimirArvore()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
