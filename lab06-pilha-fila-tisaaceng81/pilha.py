from vetor import vetor
import random

class pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.tamanho = 0
        self.dados = vetor(capacidade)

    def empilhar(self, valor):
        if self.tamanho == self.capacidade:
            raise Exception("Pilha cheia")
        # usa o método inserir do vetor circular
        self.dados.inserir(valor)
        self.tamanho += 1

    def desempilhar(self):
        if self.tamanho == 0:
            raise Exception("Pilha vazia")
        # calcula índice real do topo no vetor circular
        pos_topo = (self.dados.inicio + self.tamanho - 1) % self.capacidade
        valor = self.dados.dados[pos_topo]
        # "remove" o topo apenas limpando e diminuindo tamanho lógico
        self.dados.dados[pos_topo] = None
        self.tamanho -= 1
        return valor

    def topo(self):
        if self.tamanho == 0:
            raise Exception("Pilha vazia")
        pos_topo = (self.dados.inicio + self.tamanho - 1) % self.capacidade
        return self.dados.dados[pos_topo]

    def imprimir_vertical(self):
        print("Pilha (topo acima):")
        for i in range(self.tamanho - 1, -1, -1):
            pos = (self.dados.inicio + i) % self.capacidade
            print(self.dados.dados[pos])

    def tamanho_pilha(self):
        return self.tamanho

    def capacidade_pilha(self):
        return self.capacidade

def main():
    p = pilha(10)
    # empilha valores aleatórios
    for _ in range(10):
        p.empilhar(random.randint(1, 100))

    # imprime estado inicial
    p.imprimir_vertical()
    print("Topo:", p.topo())
    print("Tamanho:", p.tamanho_pilha())
    print("Capacidade:", p.capacidade_pilha())
    print()

    # desempilha um a um, mostrando estado
    while p.tamanho > 0:
        print("Desempilhando:", p.desempilhar())
        p.imprimir_vertical()
        print()
if __name__ == "__main__":
    main()
