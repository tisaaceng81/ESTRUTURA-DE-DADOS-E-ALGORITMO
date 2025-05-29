# Lab 07 - Pilhas e Filas
# Criando uma Classe Fila


# *******************************************************
# ***                                                 ***
# *******************************************************
class vetorCircular:
    def __init__(self, quantidade_maxima):
        self.quantidade_maxima = quantidade_maxima
        self.dados = [0] * quantidade_maxima
        self.inicio = 0
        self.fim = 0
        self.tamanho = 0

    def inserir(self, elemento):
        if self.cheio():
            raise OverflowError("Vetor circular cheio.")
        self.dados[self.fim] = elemento
        self.fim = (self.fim + 1) % self.quantidade_maxima
        self.tamanho += 1

    def remover(self):
        if self.vazio():
            raise IndexError("Vetor circular vazio.")
        elemento = self.dados[self.inicio]
        self.dados[self.inicio] = 0  
        self.inicio = (self.inicio + 1) % self.quantidade_maxima
        self.tamanho -= 1
        return elemento

    def cheio(self):
        return self.tamanho == self.quantidade_maxima

    def vazio(self):
        return self.tamanho == 0

    def __str__(self):
        elementos = []
        i = self.inicio
        count = 0
        while count < self.tamanho:
            elementos.append(str(self.dados[i]))
            i = (i + 1) % self.quantidade_maxima
            count += 1
        return "[" + ", ".join(elementos) + "]"


class cFila:
    def __init__(self, quantidade_maxima):
        self.dados = vetorCircular(quantidade_maxima)

    def queue(self, elemento):
        try:
            self.dados.inserir(elemento)
        except OverflowError:
            print("Fila cheia!")

    def dequeue(self):
        try:
            return self.dados.remover()
        except IndexError:
            print("Fila vazia!")

    def vazia(self):
        return self.dados.vazio()

    def cheia(self):
        return self.dados.cheio()

    def __str__(self):
        return str(self.dados)


if __name__ == '__main__':
    numElementos = 10
    fila = cFila(numElementos)

    i = 100
    while numElementos > 0:
        fila.queue(i)
        print(f'++ {i}')
        i += 3
        numElementos -= 1

    while not fila.vazia():
        i = fila.dequeue()
        print(f'-- {i}')
