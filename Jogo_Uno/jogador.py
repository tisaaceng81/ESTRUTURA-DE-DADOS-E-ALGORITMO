from cartas import Vetor, Carta

# Função para colorir cartas (mesma usada em cartas.py)
def carta_colorida_texto(carta):
    cores_rgb = {
        "Vermelho": (255, 0, 0),
        "Amarelo": (255, 255, 0),
        "Azul": (0, 0, 255),
        "Verde": (0, 128, 0),
    }
    cor = carta.cor.capitalize() if hasattr(carta, 'cor') else ""
    texto = str(carta)
    if cor in cores_rgb:
        r, g, b = cores_rgb[cor]
        return f"\033[38;2;{r};{g};{b}m{texto}\033[0m"
    else:
        return texto

class Jogador:
    def __init__(self, nome, humano=False):
        self.nome = nome
        self.humano = humano
        self.mao = Vetor(capacidade=50)  

    def comprar_carta(self, carta):
        if carta is not None:
            self.mao.inserir(carta)
            return True
        return False

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
            print(f"[{i}] {carta_colorida_texto(self.mao[i])}")

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

    jogador = Jogador("Jogador 1")

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
