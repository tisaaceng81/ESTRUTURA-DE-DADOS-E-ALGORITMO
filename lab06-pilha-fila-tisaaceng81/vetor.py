class vetor:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.tamanho = 0
        self.dados = [0] * capacidade
        self.inicio = 0
        self.fim = 0

    def inserir(self, valor):
        if self.tamanho == self.capacidade:
            raise Exception("Vetor cheio")
        self.dados[self.fim] = valor
        self.fim = (self.fim + 1) % self.capacidade
        self.tamanho += 1

    def remover(self):
        if self.tamanho == 0:
            raise Exception("Vetor vazio")
        valor = self.dados[self.inicio]
        self.dados[self.inicio] = 0
        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho -= 1
        return valor

    def obter(self, posicao):
        if posicao < 0 or posicao >= self.tamanho:
            raise Exception("Posição inválida")
        return self.dados[(self.inicio + posicao) % self.capacidade]

    def tamanho_vetor(self):
        return self.tamanho

    def capacidade_vetor(self):
        return self.capacidade

    def __str__(self):
        # Apenas para debug, imprime do primeiro elemento válido até o fim
        resultado = "["
        for i in range(self.tamanho):
            if i > 0:
                resultado += ","
            resultado += str(self.dados[(self.inicio + i) % self.capacidade])
        resultado += "]"
        return resultado
if __name__ == "__main__":
    # Testando a classe vetor
    v = vetor(5)
    v.inserir(1)
    v.inserir(2)
    v.inserir(3)
    print(v)  # Deve imprimir [1, 2, 3]
    v.remover()
    print(v)  # Deve imprimir [2, 3]
    v.inserir(4)
    v.inserir(5)
    print(v)  # Deve imprimir [2, 3, 4, 5]
    v.remover()
    print(v)  # Deve imprimir [3, 4, 5]
    
