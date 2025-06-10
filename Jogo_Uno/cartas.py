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

# Função para colorir as cartas vermelhas, amarelas, verdes e azuis usando ANSI RGB
def carta_colorida_texto(carta):
    cores_rgb = {
        "VM": (255, 0, 0),
        "AM": (255, 255, 0),
        "AZ": (0, 0, 255),
        "VD": (0, 128, 0),
    }
    cor = carta.cor.capitalize() if hasattr(carta, 'cor') else ""
    texto = str(carta)
    if cor in cores_rgb:
        r, g, b = cores_rgb[cor]
        return f"\033[38;2;{r};{g};{b}m{texto}\033[0m"
    else:
        return texto

def mostrar_mao(mao):
    if mao.tamanho == 0:
        return "vazia"
    resultado = ""
    for i in range(mao.tamanho):
        resultado += carta_colorida_texto(mao[i])
        if i < mao.tamanho - 1:
            resultado += ", "
    return resultado

def mostrar_deck_(baralho, max_por_linha=5):
    if baralho.vazio():
        return "Baralho vazio"
    linhas = Vetor(capacidade=(baralho.tamanho // max_por_linha + 1))
    linha_atual = ""
    cont = 0
    for i in range(baralho.tamanho):
        linha_atual += carta_colorida_texto(baralho[i])
        cont += 1
        if cont < max_por_linha and i < baralho.tamanho - 1:
            linha_atual += ", "
        if cont == max_por_linha or i == baralho.tamanho - 1:
            linhas.inserir(linha_atual)
            linha_atual = ""
            cont = 0
    resultado = ""
    for i in range(linhas.tamanho):
        resultado += linhas[i] + "\n"
    return resultado.rstrip("\n")

if __name__ == "__main__":
    print("=== Teste módulo cartas ===")

    baralho = criar_baralho()
    print(f"Total de cartas no baralho: {baralho.tamanho}")
    embaralhar(baralho)

    num_cartas = 7
    print(f"Removendo {num_cartas} cartas do baralho para simular mão inicial:")
    mao_inicial = Vetor(capacidade=num_cartas)  
    for _ in range(num_cartas):
        carta = baralho.remover()
        if carta:
            mao_inicial.inserir(carta)

    print("Mão inicial:")
    print(mostrar_mao(mao_inicial))

    print(f"Cartas restantes no baralho: {baralho.tamanho}")
    print("Embaralhando a mão inicial...")
    embaralhar(mao_inicial)
    print("Mão embaralhada:")
    print(mostrar_mao(mao_inicial))
