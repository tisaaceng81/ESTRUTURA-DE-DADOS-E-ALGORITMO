# vetor.py
# Implementa uma estrutura de array limitado, que não cresce automaticamente.
# Não usa listas nativas do Python para armazenamento interno.
# Permite adicionar e obter elementos por índice, com limite fixo de capacidade.

class ArrayLimitado:
    def __init__(self, capacidade):
        """
        Inicializa o ArrayLimitado com capacidade fixa.
        """
        self.capacidade = capacidade
        self.itens = [None] * capacidade  # Array fixo com None inicialmente
        self.tamanho_atual = 0             # Quantidade atual de elementos adicionados

    def adicionar(self, indice, valor):
        """
        Adiciona o valor na posição especificada se dentro da capacidade.
        Se indice == tamanho_atual, significa adicionar no final.
        """
        if indice < 0 or indice >= self.capacidade:
            raise IndexError("Índice fora do limite da capacidade")
        if indice > self.tamanho_atual:
            raise IndexError("Índice inválido para adicionar")
        self.itens[indice] = valor
        # Atualiza o tamanho se adicionou na próxima posição disponível
        if indice == self.tamanho_atual:
            self.tamanho_atual += 1

    def obter(self, indice):
        """
        Retorna o elemento armazenado no índice dado.
        """
        if indice < 0 or indice >= self.tamanho_atual:
            raise IndexError("Índice fora do tamanho atual")
        return self.itens[indice]

    def resetar(self):
        """
        Reseta o array para estado vazio, mas mantém a capacidade.
        """
        self.itens = [None] * self.capacidade
        self.tamanho_atual = 0

    def __len__(self):
        """
        Retorna o número de elementos efetivamente armazenados.
        """
        return self.tamanho_atual
