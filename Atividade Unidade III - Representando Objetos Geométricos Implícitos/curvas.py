# curvas.py
# Define várias curvas implícitas e armazena seus nomes e equações
# em estruturas do tipo ArrayLimitado, evitando listas nativas.

from vetor import ArrayLimitado  # Importa a estrutura limitada
import math

# Equação de uma superelipse
def superelipse_eq(x, y, a=1.5, b=1.0, n=2.5):
    return (abs(x/a)**n + abs(y/b)**n) - 1

# Equação quártica
def quartica_eq(x, y):
    return (x**4 + y**4) - 1

# Equação da lemniscata
def lemniscata_eq(x, y):
    return (x**2 + y**2)**2 - 2*(x**2 - y**2)

# Equação de um coração
def coracao_eq(x, y):
    return ((x**2 + y**2 - 1)**3) - (x**2)*(y**3)

# Equação aproximada da silhueta de um coelho
def coelho_eq(x, y):
    y = -y
    corpo = ((x)/1.0)**2 + ((y+0.3)/0.7)**2 - 1
    cabeca = ((x-1.0)/0.5)**2 + ((y+0.6)/0.5)**2 - 1
    orelha1 = ((x-1.15)/0.15)**2 + ((y+1.0)/0.4)**2 - 1
    orelha2 = ((x-0.85)/0.15)**2 + ((y+1.0)/0.4)**2 - 1
    menor_valor = corpo
    if cabeca < menor_valor:
        menor_valor = cabeca
    if orelha1 < menor_valor:
        menor_valor = orelha1
    if orelha2 < menor_valor:
        menor_valor = orelha2
    return menor_valor

# Equação aproximada da silhueta de um gato
def gato_eq(x, y):
    y = -y
    corpo = ((x+0.2)/1.0)**2 + ((y+0.1)/0.6)**2 - 1
    cabeca = ((x-0.8)/0.5)**2 + ((y+0.5)/0.5)**2 - 1
    orelha1 = ((x-0.95)/0.15)**2 + ((y+0.9)/0.3)**2 - 1
    orelha2 = ((x-0.65)/0.15)**2 + ((y+0.9)/0.3)**2 - 1
    cauda = ((x+1.1)/0.3)**2 + ((y-0.3)/0.8)**2 - 1
    menor_valor = corpo
    if cabeca < menor_valor:
        menor_valor = cabeca
    if orelha1 < menor_valor:
        menor_valor = orelha1
    if orelha2 < menor_valor:
        menor_valor = orelha2
    if cauda < menor_valor:
        menor_valor = cauda
    return menor_valor

# Lista de curvas usando ArrayLimitado
lista_curvas = ArrayLimitado(6)

# Adiciona os pares (nome, função) como ArrayLimitado de 2 posições
item0 = ArrayLimitado(2)
item0.adicionar(0, "Superelipse")
item0.adicionar(1, superelipse_eq)
lista_curvas.adicionar(0, item0)

item1 = ArrayLimitado(2)
item1.adicionar(0, "Quártica")
item1.adicionar(1, quartica_eq)
lista_curvas.adicionar(1, item1)

item2 = ArrayLimitado(2)
item2.adicionar(0, "Lemniscata")
item2.adicionar(1, lemniscata_eq)
lista_curvas.adicionar(2, item2)

item3 = ArrayLimitado(2)
item3.adicionar(0, "Coração")
item3.adicionar(1, coracao_eq)
lista_curvas.adicionar(3, item3)

item4 = ArrayLimitado(2)
item4.adicionar(0, "Coelho")
item4.adicionar(1, coelho_eq)
lista_curvas.adicionar(4, item4)

item5 = ArrayLimitado(2)
item5.adicionar(0, "Gato")
item5.adicionar(1, gato_eq)
lista_curvas.adicionar(5, item5)
