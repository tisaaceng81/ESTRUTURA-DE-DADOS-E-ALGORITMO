# estrutura.py

# ---------- TAD No ----------
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


# ---------- TAD Pilha (Lista Encadeada) ----------
class Pilha:
    def __init__(self):
        self.topo = None

    def push(self, valor):
        print(f"Push: {valor}")
        novo = No(valor)
        novo.proximo = self.topo
        self.topo = novo
        self.exibir()

    def pop(self):
        if self.topo is None:
            return None
        valor = self.topo.dado
        self.topo = self.topo.proximo
        print(f"Pop: {valor}")
        self.exibir()
        return valor

    def esta_vazia(self):
        return self.topo is None

    def exibir(self):
        atual = self.topo
        elementos = []
        while atual:
            elementos.append(atual.dado)
            atual = atual.proximo
        print("Pilha: ", elementos)


# ---------- Fila com duas pilhas ----------
class FilaComDuasPilhas:
    def __init__(self):
        self.entrada = Pilha()
        self.saida = Pilha()

    def enfileirar(self, valor):
        print(f"Enfileirar: {valor}")
        self.entrada.push(valor)

    def desenfileirar(self):
        if self.saida.esta_vazia():
            while not self.entrada.esta_vazia():
                self.saida.push(self.entrada.pop())
        return self.saida.pop()


# ---------- TAD Fila (Lista Encadeada) ----------
class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enfileirar(self, valor):
        print(f"Enfileirar: {valor}")
        novo = No(valor)
        if self.fim is None:
            self.inicio = self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
        self.exibir()

    def desenfileirar(self):
        if self.inicio is None:
            return None
        valor = self.inicio.dado
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        print(f"Desenfileirar: {valor}")
        self.exibir()
        return valor

    def esta_vazia(self):
        return self.inicio is None

    def exibir(self):
        atual = self.inicio
        elementos = []
        while atual:
            elementos.append(atual.dado)
            atual = atual.proximo
        print("Fila: ", elementos)


# ---------- Pilha com duas filas ----------
class PilhaComDuasFilas:
    def __init__(self):
        self.q1 = Fila()
        self.q2 = Fila()

    def push(self, valor):
        print(f"Push (PilhaComDuasFilas): {valor}")
        self.q2.enfileirar(valor)
        while not self.q1.esta_vazia():
            self.q2.enfileirar(self.q1.desenfileirar())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.desenfileirar()


# ---------- Remover recursivamente caracteres adjacentes duplicados ----------
def remover_adj_duplicados(s):
    print(f"Processando: {s}")
    if len(s) <= 1:
        return s

    i = 0
    while i < len(s) - 1 and s[i] == s[i + 1]:
        i += 1

    if i > 0:
        return remover_adj_duplicados(s[i + 1:])
    else:
        return s[0] + remover_adj_duplicados(s[1:])


# ---------- Maior soma em janela deslizante ----------
def maior_soma_janela(vetor, k):
    if k <= 0 or len(vetor) < k:
        return None

    soma_atual = 0
    maior_soma = float('-inf')

    for i in range(len(vetor)):
        soma_atual += vetor[i]
        if i >= k:
            soma_atual -= vetor[i - k]
        if i >= k - 1:
            print(f"Janela {vetor[i-k+1:i+1]}: soma = {soma_atual}")
            if soma_atual > maior_soma:
                maior_soma = soma_atual

    return maior_soma


# ---------- TAD Fila Circular ----------
class FilaCircular:
    def __init__(self, capacidade):
        self.vetor = [None] * capacidade
        self.capacidade = capacidade
        self.inicio = 0
        self.fim = 0
        self.tamanho = 0

    def enfileirar(self, valor):
        if self.tamanho == self.capacidade:
            print("Fila cheia!")
            return False
        self.vetor[self.fim] = valor
        self.fim = (self.fim + 1) % self.capacidade
        self.tamanho += 1
        self.exibir()
        return True

    def desenfileirar(self):
        if self.tamanho == 0:
            print("Fila vazia!")
            return None
        valor = self.vetor[self.inicio]
        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho -= 1
        self.exibir()
        return valor

    def esta_vazia(self):
        return self.tamanho == 0

    def exibir(self):
        elementos = []
        i = self.inicio
        count = 0
        while count < self.tamanho:
            elementos.append(self.vetor[i])
            i = (i + 1) % self.capacidade
            count += 1
        print("Fila Circular: ", elementos)


# ---------- Testes principais ----------
if __name__ == "__main__":
    print("\n--- Remover duplicados ---")
    print(remover_adj_duplicados("careermonk"))  # camonk
    print(remover_adj_duplicados("mississippi"))  # m

    print("\n--- Maior soma em janela ---")
    print("Maior soma:", maior_soma_janela([1, 3, -1, -3, 5, 3, 6, 7], 3))  # 16

    print("\n--- Fila circular ---")
    fila = FilaCircular(3)
    fila.enfileirar(10)
    fila.enfileirar(20)
    fila.enfileirar(30)
    fila.enfileirar(40)  # Fila cheia
    fila.desenfileirar()  # 10
    fila.desenfileirar()  # 20
    fila.desenfileirar()  # 30
    fila.desenfileirar()  # Fila vazia

    print("\n--- Fila com duas pilhas ---")
    fdp = FilaComDuasPilhas()
    fdp.enfileirar(1)
    fdp.enfileirar(2)
    fdp.enfileirar(3)
    print("Desenfileirado:", fdp.desenfileirar())
    print("Desenfileirado:", fdp.desenfileirar())

    print("\n--- Pilha com duas filas ---")
    pdf = PilhaComDuasFilas()
    pdf.push(10)
    pdf.push(20)
    pdf.push(30)
    print("Desempilhado:", pdf.pop())
    print("Desempilhado:", pdf.pop())
