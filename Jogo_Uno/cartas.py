import random

class Carta:
    def __init__(self, cor, valor):
        self.cor = cor
        self.valor = valor

    def __repr__(self):
        return f"{self.cor} {self.valor}"

    def combina_com(self, outra):
        return (self.cor == outra.cor or
                self.valor == outra.valor or
                self.cor == "Preto" or
                outra.cor == "Preto")

class Vetor:
    def __init__(self, capacidade=100):
        self._dados = [None] * capacidade  
        self.tamanho = 0
        self.capacidade = capacidade

    def inserir(self, item):
        if self.tamanho >= self.capacidade:
            raise Exception("Capacidade do vetor excedida")
        self._dados[self.tamanho] = item
        self.tamanho += 1

    def remover(self):
        if self.vazio():
            return None
        self.tamanho -= 1
        item = self._dados[self.tamanho]
        self._dados[self.tamanho] = None  
        return item

    def __getitem__(self, idx):
        if 0 <= idx < self.tamanho:
            return self._dados[idx]
        return None

    def __setitem__(self, idx, valor):
        if 0 <= idx < self.tamanho:
            self._dados[idx] = valor

    def vazio(self):
        return self.tamanho == 0

    def limpar(self):
        for i in range(self.tamanho):
            self._dados[i] = None
        self.tamanho = 0

def carta_colorida_texto(carta):
    cores = {
        "Vermelho": "\033[91m",
        "Verde": "\033[92m",
        "Amarelo": "\033[93m",
        "Azul": "\033[94m",
        "Preto": "\033[90m"
    }
    reset = "\033[0m"
    return f"{cores.get(carta.cor, '')}{carta.cor} {carta.valor}{reset}"

def criar_baralho():
    baralho = Vetor(capacidade=120)  
    cores = ["Vermelho", "Amarelo", "Verde", "Azul"]
    valores = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Pular", "Reverter", "+2"]

    for cor in cores:
        baralho.inserir(Carta(cor, "0"))
        for valor in valores[1:]:
            baralho.inserir(Carta(cor, valor))
            baralho.inserir(Carta(cor, valor))

    for _ in range(4):
        baralho.inserir(Carta("Preto", "Coringa"))
        baralho.inserir(Carta("Preto", "+4"))

    return baralho

def embaralhar(vetor):
    n = vetor.tamanho
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        vetor[i], vetor[j] = vetor[j], vetor[i]

def mostrar_mao(mao):
    if mao.tamanho == 0:
        return "vazia"
    resultado = ""
    for i in range(mao.tamanho):
        resultado += carta_colorida_texto(mao[i])
        if i < mao.tamanho - 1:
            resultado += ", "
    return resultado

if __name__ == "__main__":
    print("=== Teste módulo cartas ===")
    baralho = criar_baralho()
    print(f"Total de cartas no baralho: {baralho.tamanho}")
    embaralhar(baralho)
    mao_inicial = Vetor(capacidade=7)
    for _ in range(7):
        carta = baralho.remover()
        if carta:
            mao_inicial.inserir(carta)
    print("Mão inicial:")
    print(mostrar_mao(mao_inicial))