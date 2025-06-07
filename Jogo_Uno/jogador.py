from cartas import Vetor, Carta

class Jogador:
    def __init__(self, nome, humano=False):
        self.nome = nome
        self.humano = humano
        self.mao = Vetor(capacidade=50)  # capacidade fixa para a mão

    def comprar_carta(self, carta):
        """
        Recebe uma carta (já removida do baralho) e insere na mão.
        Retorna True se inseriu, False caso receba None.
        """
        if carta is not None:
            self.mao.inserir(carta)
            return True
        return False

    # Método alternativo, só para manter o nome que você usou no simulador
    comprar_carta_com_baralho = comprar_carta

    def remover_carta(self, carta):
        for i in range(self.mao.tamanho):
            if self.mao[i] == carta:
                for j in range(i, self.mao.tamanho - 1):
                    self.mao[j] = self.mao[j + 1]
                self.mao.tamanho -= 1
                return

    def mostrar_mao(self):
        for i in range(self.mao.tamanho):
            print(f"[{i}] {self.mao[i]}")

    def get_carta(self, idx):
        return self.mao[idx] if 0 <= idx < self.mao.tamanho else None

    def tem_carta_valida(self, carta_mesa):
        for i in range(self.mao.tamanho):
            if self.mao[i].combina_com(carta_mesa):
                return True
        return False

    def escolher_carta(self, carta_mesa):
        for i in range(self.mao.tamanho):
            if self.mao[i].combina_com(carta_mesa):
                carta = self.mao[i]
                self.remover_carta(carta)
                return carta
        return None

    def mao_vazia(self):
        return self.mao.tamanho == 0


if __name__ == "__main__":
    from cartas import criar_baralho, embaralhar

    print("=== Teste módulo jogador ===")

    baralho = criar_baralho()
    embaralhar(baralho)

    jogador = Jogador("Alice")

    num_cartas = 7
    print(f"Jogador comprando {num_cartas} cartas do baralho...")
    for _ in range(num_cartas):
        carta = baralho.remover()
        if carta:
            jogador.comprar_carta_com_baralho(carta)
        else:
            print("Baralho vazio! Não pode comprar mais cartas.")
            break

    print("Mão do jogador após compra:")
    jogador.mostrar_mao()
    print(f"Cartas restantes no baralho: {baralho.tamanho}")
