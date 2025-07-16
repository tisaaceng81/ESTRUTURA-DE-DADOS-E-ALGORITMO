# vetor.py
# Implementa uma estrutura de vetor com capacidade fixa,
# para substituir listas nativas, conforme usado em seus módulos.

class ArrayLimitado:
    def __init__(self, capacidade):
        """
        Inicializa o vetor limitado com uma capacidade fixa.
        """
        self.capacidade = capacidade                # Capacidade máxima do vetor
        self.dados = [None] * capacidade            # Lista interna para armazenar os elementos
        self.tamanho = 0                            # Quantidade atual de elementos armazenados

    def adicionar(self, indice, valor):
        """
        Adiciona um valor no índice especificado, deslocando os elementos à direita.
        """
        if self.tamanho >= self.capacidade:
            raise Exception("Capacidade máxima atingida.")    # Evita overflow
        if indice < 0 or indice > self.tamanho:
            raise IndexError("Índice fora do intervalo para inserção.")  # Valida índice
        
        # Desloca elementos para a direita para abrir espaço na posição 'indice'
        for i in range(self.tamanho, indice, -1):
            self.dados[i] = self.dados[i - 1]
        
        self.dados[indice] = valor   # Insere o novo valor
        self.tamanho += 1            # Incrementa tamanho atual

    def remover(self, indice):
        """
        Remove o elemento no índice especificado, deslocando elementos à esquerda para preencher o vazio.
        """
        if indice < 0 or indice >= self.tamanho:
            raise IndexError("Índice fora do intervalo para remoção.")  # Valida índice
        
        # Desloca elementos para a esquerda para preencher a lacuna
        for i in range(indice, self.tamanho - 1):
            self.dados[i] = self.dados[i + 1]
        
        self.dados[self.tamanho - 1] = None  # Limpa a última posição
        self.tamanho -= 1                    # Decrementa o tamanho atual

    def obter(self, indice):
        """
        Retorna o elemento armazenado no índice especificado.
        """
        if 0 <= indice < self.tamanho:
            return self.dados[indice]
        else:
            raise IndexError("Índice fora do intervalo.")  # Valida índice

    def __len__(self):
        """
        Retorna o número atual de elementos no vetor.
        """
        return self.tamanho

    def resetar(self):
        """
        Limpa o vetor, removendo todos os elementos e zerando tamanho.
        """
        self.dados = [None] * self.capacidade
        self.tamanho = 0
