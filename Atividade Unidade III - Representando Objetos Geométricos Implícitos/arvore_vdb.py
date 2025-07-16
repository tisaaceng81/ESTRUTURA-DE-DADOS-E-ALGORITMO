from no_vdb import NodoVDB  # Importa a classe NodoVDB que representa cada nó da árvore

class EstruturaVDB:
    def __init__(self, limite_profundidade, tamanho_espaco):
        # Limite máximo de profundidade da subdivisão da árvore
        self.limite_profundidade = limite_profundidade
        # Tamanho do espaço quadrado que será subdividido
        self.tamanho_espaco = tamanho_espaco
        # Cria o nó raiz centralizado na origem, com nível 0
        self.raiz = NodoVDB(-tamanho_espaco/2, -tamanho_espaco/2, tamanho_espaco, tamanho_espaco, 0)

    def construir_estrutura(self, funcao_curva):
        # Inicia o processo recursivo de divisão da árvore usando a função da curva
        self.raiz.dividir(self.limite_profundidade, funcao_curva)
