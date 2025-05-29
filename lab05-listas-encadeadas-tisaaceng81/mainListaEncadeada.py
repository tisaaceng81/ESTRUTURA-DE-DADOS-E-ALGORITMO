# ##################################################
# Programa de teste para uma lista encadeada
# ##################################################

import cNo
import cListaEncadeada

import sys
import random
import math

from datetime import datetime

# *******************************************************
# ***                                                 ***
# *******************************************************
def trataLinhaDeComando():
    n = 10
    if (len(sys.argv) > 1):
        n = int(sys.argv[1])
        if n < 0:
            n = 10
    return n

# *******************************************************
# ***                                                 ***
# *******************************************************
# Lê quantidade de elementos
numElementos = trataLinhaDeComando()

# Cria a lista encadeada
lista = cListaEncadeada.cLSE()

print("Lista antes da inserção:")
print(lista)

# Geração e inserção ordenada
print(f"Inserindo {numElementos} elementos (ordem crescente)...")
random.seed(42)  # para resultados reprodutíveis
elementos = [random.randint(1, 99) for _ in range(numElementos)]
print("Elementos gerados:", elementos)

for valor in elementos:
    lista.insereOrdenado(valor)

print("\nLista após inserções ordenadas:")
print(lista)

# Teste de busca
valorBusca = elementos[numElementos // 2] if numElementos > 0 else 0
print(f"Buscando valor {valorBusca}:")
if lista.buscaDado(valorBusca):
    print("→ Busca com sucesso.")
else:
    print("→ Busca sem sucesso.")

# Teste de remoção
valorRemover = elementos[0] if numElementos > 0 else 0
print(f"Tentando remover valor {valorRemover}:")
if lista.removeDado(valorRemover):
    print("→ Remoção com sucesso.")
else:
    print("→ Remoção sem sucesso.")

print("\nLista após tentativa de remoção:")
print(lista)

print(f"Tamanho final da lista: {lista.getTamanho()}")
