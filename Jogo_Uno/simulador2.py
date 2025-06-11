import sys
import time
import random
from cartas import criar_baralho, embaralhar, Vetor, Carta
from jogador import Jogador

def carta_colorida_texto(carta):
    cores_ansi = {
        "Vermelho": ("\033[91m", "C "),
        "Amarelo": ("\033[93m", "C "),
        "Azul": ("\033[94m", "C "),
        "Verde": ("\033[92m", "C "),
    }

    cor = carta.cor.capitalize() if hasattr(carta, 'cor') else ""
    valor = str(carta.valor) if hasattr(carta, 'valor') else "C "

    if cor in cores_ansi:
        cor_ansi, letra_cor = cores_ansi[cor]
        return f"{cor_ansi}{letra_cor}{valor}\033[0m"
    else:
        return f"C{valor}"  
    if cor == "Amarelo":
        if carta.valor == "6":
            texto_valor = "C-(6)"
        elif carta.valor == "+2":
            texto_valor = "C (+2)"
        else:
            texto_valor = f"C-({carta.valor})"
    elif cor == "Azul":
        if carta.valor == "5":
            texto_valor = "C-(5)"
        elif carta.valor.lower() == "pular":
            texto_valor = "C-(Pular)"
        else:
            texto_valor = f"C-({carta.valor})"
    elif cor == "Vermelho":
        if carta.valor.lower() == "reverter":
            texto_valor = "C-Reverter"
        else:
            texto_valor = f"C-({carta.valor})"
    elif cor == "Preto":
        if carta.valor == "+4":
            texto_valor = "C (+4)"
        else:
            texto_valor = f"C-({carta.valor})"
    elif cor == "Coringa":
        texto_valor = f"{carta.valor}"
    
    elif cor == "Verde":
        if carta.valor.lower() == "reverter":
            texto_valor = "C-Reverter"
        else:
            texto_valor = f"C ({carta.valor})"
    else:
        
        texto_valor = f"{carta.valor}({cor})"

    cor_ansi = cores_ansi.get(cor, reset)

    return f"{cor_ansi}{texto_valor}{reset}"


def mostrar_mao(jogador):
    if jogador.mao.tamanho == 0:
        return "vazia"
    resultado = ""
    for i in range(jogador.mao.tamanho):
        resultado += carta_colorida_texto(jogador.mao[i])
        if i < jogador.mao.tamanho - 1:
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

def aplicar_efeito_carta(carta, indice_atual, sentido, jogadores, baralho):
    valor = carta.valor
    prox = (indice_atual + sentido) % jogadores.tamanho

    if valor == "Pular":
        novo_indice = (prox + sentido) % jogadores.tamanho
        novo_sentido = sentido
        print(f"{jogadores[prox].nome} foi pulado!")
        time.sleep(3)
    elif valor == "Reverter":
        novo_sentido = -sentido
        novo_indice = (indice_atual + novo_sentido) % jogadores.tamanho
        print("Sentido do jogo invertido!")
        time.sleep(3)
    elif valor == "+2":
        for _ in range(3):
            if not baralho.vazio():
                carta_comprada = baralho.remover()
                jogadores[prox].comprar_carta_com_baralho(carta_comprada)
        print(f"{jogadores[prox].nome} comprou 2 cartas e perdeu a vez!")
        time.sleep(3)
        novo_indice = (prox + sentido) % jogadores.tamanho
        novo_sentido = sentido
    elif valor == "+4":
        for _ in range(4):
            if not baralho.vazio():
                carta_comprada = baralho.remover()
                jogadores[prox].comprar_carta_com_baralho(carta_comprada)
        print(f"{jogadores[prox].nome} comprou 4 cartas e perdeu a vez!")
        time.sleep(3)
        novo_indice = (prox + sentido) % jogadores.tamanho
        novo_sentido = sentido
    else:
        novo_indice = prox
        novo_sentido = sentido

    return novo_indice, novo_sentido

def sortear_jogador_inicial(jogadores):
    print("\n🔄 Sorteando quem começa o jogo...\n")
    time.sleep(1)

    voltas = random.randint(10, 20)
    for i in range(voltas):
        indice = i % jogadores.tamanho
        nome = jogadores[indice].nome
        print(f"🎯 {nome}", end="\r", flush=True)
        time.sleep(0.1 + (i / voltas) * 0.08)

    escolhido = random.randint(0, jogadores.tamanho - 1)
    nome_escolhido = jogadores[escolhido].nome
    print(f"\n✅ {nome_escolhido} foi sorteado para começar!{' ' * 20}\n")
    time.sleep(2)
    return escolhido

def main():
    if len(sys.argv) > 1:
        try:
            num_jogadores = int(sys.argv[1])
            if not (5 <= num_jogadores <= 10):
                raise ValueError
        except ValueError:
            print("Número inválido. Informe um número entre 5 e 10.")
            return
    else:
        num_jogadores = 7

    baralho = criar_baralho()
    embaralhar(baralho)

    jogadores = Vetor(capacidade=10)
    jogadores.inserir(Jogador("Você", humano=True))
    for i in range(1, num_jogadores):
        jogadores.inserir(Jogador(f"Jogador {i}"))

    # Distribuir cartas
    for _ in range(7):
        for j in range(jogadores.tamanho):
            carta = baralho.remover()
            jogadores[j].comprar_carta_com_baralho(carta)

    carta_mesa = baralho.remover()
    cartas_jogadas = Vetor(capacidade=108)
    cartas_jogadas.inserir(carta_mesa)

    print("\nCarta inicial na mesa:", carta_colorida_texto(carta_mesa))
    time.sleep(2)

    indice_jogador = sortear_jogador_inicial(jogadores)
    sentido = 1

    while True:
        print("\n========================================")
        print(f"Pilha de compra (deck) [{baralho.tamanho} cartas]:")
        print(mostrar_deck_(baralho))
        print()
        if not baralho.vazio():
            print(f"Carta no topo do deck para compra: {carta_colorida_texto(baralho[baralho.tamanho-1])}")
        print(f"\nCartas descartadas [{cartas_jogadas.tamanho}]:")
        print(mostrar_deck_(cartas_jogadas))
        print(f"\nCarta atual na mesa: {carta_colorida_texto(carta_mesa)}\n")

        print("Estado das mãos dos jogadores:")
        for i in range(jogadores.tamanho):
            jogador = jogadores[i]
            print(f" - {jogador.nome}: {mostrar_mao(jogador)}")
        print()

        jogador_atual = jogadores[indice_jogador]
        print(f"{jogador_atual.nome}, sua vez!")
        time.sleep(3)

        if jogador_atual.humano:
            print("Sua mão:")
            for i in range(jogador_atual.mao.tamanho):
                print(f"[{i}] {carta_colorida_texto(jogador_atual.mao[i])}")

            while True:
                escolha = input("Digite o índice da carta para jogar ou 'comprar': ").strip().lower()
                if escolha == "comprar":
                    if not baralho.vazio():
                        nova = baralho.remover()
                        print(f"Você comprou: {carta_colorida_texto(nova)}")
                        jogador_atual.comprar_carta_com_baralho(nova)
                        time.sleep(3)
                        if nova.combina_com(carta_mesa):
                            print("Carta jogada automaticamente!")
                            carta_mesa = nova
                            cartas_jogadas.inserir(nova)
                            jogador_atual.remover_carta(nova)
                        else:
                            print("Não pode jogar essa carta agora. Passando a vez.")
                    else:
                        print("Baralho vazio!")
                    break
                elif escolha.isdigit():
                    idx = int(escolha)
                    carta = jogador_atual.get_carta(idx)
                    if carta and carta.combina_com(carta_mesa):
                        if carta.valor in ["Coringa", "+4"]:
                            cores = ["vermelho", "amarelo", "azul", "verde"]
                            while True:
                                cor_escolhida = input("Escolha uma cor (vermelho, amarelo, azul, verde): ").strip().lower()
                                if cor_escolhida in cores:
                                    carta.cor = cor_escolhida.capitalize()
                                    print(f"Você escolheu a cor {carta.cor}.")
                                    time.sleep(3)
                                    break
                                else:
                                    print("Cor inválida. Tente novamente.")
                        carta_mesa = carta
                        cartas_jogadas.inserir(carta)
                        jogador_atual.remover_carta(carta)
                        print(f"Você jogou {carta_colorida_texto(carta)}")
                        time.sleep(3)
                        break
                    else:
                        print("Carta inválida! Escolha outra ou compre.")
                else:
                    print("Entrada inválida! Tente novamente.")
        else:
            carta = jogador_atual.escolher_carta(carta_mesa)
            if carta:
                print(f"{jogador_atual.nome} jogou {carta_colorida_texto(carta)}")
                carta_mesa = carta
                cartas_jogadas.inserir(carta)
                jogador_atual.remover_carta(carta)
                time.sleep(3)
            else:
                if not baralho.vazio():
                    nova = baralho.remover()
                    jogador_atual.comprar_carta_com_baralho(nova)
                    print(f"{jogador_atual.nome} comprou uma carta.")
                    time.sleep(3)
                else:
                    print(f"{jogador_atual.nome} passou a vez (baralho vazio).")
                    time.sleep(3)

        if jogador_atual.mao.tamanho == 0:
            print(f"\n🎉 {jogador_atual.nome} venceu o jogo! Parabéns! 🎉")
            break

        indice_jogador, sentido = aplicar_efeito_carta(carta_mesa, indice_jogador, sentido, jogadores, baralho)

if __name__ == "__main__":
    main()