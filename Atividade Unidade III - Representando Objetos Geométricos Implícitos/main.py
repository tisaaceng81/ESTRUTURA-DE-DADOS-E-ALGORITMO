# Módulo principal - main.py
# Responsável por inicializar a interface gráfica e mostrar a árvore VDB baseada em curvas implícitas.

import sys
import pyglet
from pyglet import shapes
from vetor import ArrayLimitado
from arvore_vdb import EstruturaVDB
from curvas import lista_curvas
from pyglet.window import key
from pyglet.gl import glClearColor  # Função para definir cor de fundo da janela

LARGURA_JANELA, ALTURA_JANELA = 800, 800

def gerar_faixa(inicio, fim, passo):
    while inicio < fim:
        yield inicio
        inicio += passo

class Visualizador:
    def __init__(self, curva, largura=LARGURA_JANELA, altura=ALTURA_JANELA, profundidade=6, modo=1):
        self.largura = largura
        self.altura = altura
        self.profundidade = profundidade
        self.curva = curva
        self.janela = pyglet.window.Window(largura, altura)
        self.janela.set_caption(f"VDB - {curva.obter(0)}")
        glClearColor(1,1,1,1)
        self.batch = pyglet.graphics.Batch()
        self.formas = ArrayLimitado(10000)
        self.arvore = EstruturaVDB(profundidade, 4)
        self.arvore.construir_estrutura(curva.obter(1))
        self.modo_visualizacao = modo
        self.nivel_visualizacao = 0
        self.janela.push_handlers(
            on_draw=self.ao_desenhar,
            on_key_press=self.ao_pressionar_tecla
        )

    def ao_desenhar(self):
        self.janela.clear()
        self.formas.resetar()
        self.batch = pyglet.graphics.Batch()
        if self.modo_visualizacao == 1:
            self.desenhar_no_recursivamente(self.arvore.raiz)
        elif self.modo_visualizacao == 2:
            self.desenhar_por_nivel(self.arvore.raiz, self.nivel_visualizacao)
        elif self.modo_visualizacao == 3:
            self.desenhar_folhas_fronteira(self.arvore.raiz)
        else:
            self.desenhar_curva()
        self.desenhar_curva()
        self.batch.draw()

    def ao_pressionar_tecla(self, simbolo, modificadores):
        if simbolo == key._1:
            self.modo_visualizacao = 1
            print("Modo: Árvore completa")
        elif simbolo == key._2:
            self.modo_visualizacao = 2
            print("Modo: Por nível")
        elif simbolo == key._3:
            self.modo_visualizacao = 3
            print("Modo: Folhas na fronteira")
        elif simbolo == key._4:
            self.modo_visualizacao = 4
            print("Modo: Apenas curva")
        if self.modo_visualizacao == 2:
            if simbolo == key.UP:
                self.nivel_visualizacao = min(self.nivel_visualizacao + 1, self.profundidade)
                print(f"Nível selecionado: {self.nivel_visualizacao}")
            elif simbolo == key.DOWN:
                self.nivel_visualizacao = max(self.nivel_visualizacao - 1, 0)
                print(f"Nível selecionado: {self.nivel_visualizacao}")

    def desenhar_no_recursivamente(self, no):
        self.desenhar_retangulo(no)
        for i in range(len(no.sub_nos)):
            self.desenhar_no_recursivamente(no.sub_nos.obter(i))

    def desenhar_por_nivel(self, no, nivel):
        if no.nivel == nivel:
            self.desenhar_retangulo(no)
        elif no.nivel < nivel:
            for i in range(len(no.sub_nos)):
                self.desenhar_por_nivel(no.sub_nos.obter(i), nivel)

    def desenhar_folhas_fronteira(self, no):
        if len(no.sub_nos) > 0:
            for i in range(len(no.sub_nos)):
                self.desenhar_folhas_fronteira(no.sub_nos.obter(i))
        else:
            self.desenhar_retangulo(no)

    def desenhar_retangulo(self, no):
        escala_x = self.largura / 4
        escala_y = self.altura / 4
        x = int((no.x + 2) * escala_x)
        y = int((no.y + 2) * escala_y)
        largura = int(no.largura * escala_x)
        altura = int(no.altura * escala_y)

        paleta_cores = ArrayLimitado(7)
        paleta_cores.adicionar(0, (255, 0, 0))
        paleta_cores.adicionar(1, (0, 255, 0))
        paleta_cores.adicionar(2, (0, 0, 255))
        paleta_cores.adicionar(3, (255, 165, 0))
        paleta_cores.adicionar(4, (128, 0, 128))
        paleta_cores.adicionar(5, (0, 255, 255))
        paleta_cores.adicionar(6, (255, 192, 203))

        cor = paleta_cores.obter(no.nivel % 7)
        retangulo = shapes.Rectangle(x, y, largura, altura, color=cor, batch=self.batch)
        retangulo.opacity = 120
        self.formas.adicionar(len(self.formas), retangulo)

        linhas = ArrayLimitado(4)
        linhas.adicionar(len(linhas), shapes.Line(x, y, x+largura, y, thickness=1, color=(0,0,0), batch=self.batch))
        linhas.adicionar(len(linhas), shapes.Line(x+largura, y, x+largura, y+altura, thickness=1, color=(0,0,0), batch=self.batch))
        linhas.adicionar(len(linhas), shapes.Line(x+largura, y+altura, x, y+altura, thickness=1, color=(0,0,0), batch=self.batch))
        linhas.adicionar(len(linhas), shapes.Line(x, y+altura, x, y, thickness=1, color=(0,0,0), batch=self.batch))

        for i in range(len(linhas)):
            self.formas.adicionar(len(self.formas), linhas.obter(i))

    def desenhar_curva(self):
        escala_x = self.largura / 4
        escala_y = self.altura / 4
        passo = 0.01
        x_atual = -2
        while x_atual < 2:
            y_atual = -2
            while y_atual < 2:
                if abs(self.curva.obter(1)(x_atual, y_atual)) < 0.01:
                    px = int((x_atual + 2) * escala_x)
                    py = int((y_atual + 2) * escala_y)
                    ponto = shapes.Circle(px, py, 1, color=(0,0,0), batch=self.batch)
                    self.formas.adicionar(len(self.formas), ponto)
                y_atual += passo
            x_atual += passo

def main():
    argumentos = sys.argv[1:]
    if argumentos:
        try:
            idx = int(argumentos[0])
            if not (0 <= idx < len(lista_curvas)):
                print(f"Índice inválido. Use valores entre 0 e {len(lista_curvas)-1}")
                return
        except:
            print("O primeiro argumento deve ser um número inteiro correspondente à curva.")
            return

        modo_vis = 1
        if len(argumentos) > 1:
            try:
                modo_vis = int(argumentos[1])
                if modo_vis not in [1, 2, 3, 4]:
                    print("Modo de visualização inválido. Usando modo padrão 1.")
                    modo_vis = 1
            except:
                print("Segundo argumento deve ser um número de modo (1 a 4). Usando modo padrão 1.")

        print(f"Curva selecionada: {lista_curvas.obter(idx).obter(0)}")
        x_teste, y_teste = 1, 0
        val = lista_curvas.obter(idx).obter(1)(x_teste, y_teste)
        print(f"Valor da curva {lista_curvas.obter(idx).obter(0)} em ({x_teste},{y_teste}): {val}")

        visual = Visualizador(lista_curvas.obter(idx), modo=modo_vis)
        print("Janela aberta. Feche para encerrar.")
        pyglet.app.run()
    else:
        while True:
            print("\nCurvas disponíveis:")
            for i in range(len(lista_curvas)):
                curva = lista_curvas.obter(i)
                nome_curva = curva.obter(0)
                print(f"{i}: {nome_curva}")
            escolha = input("Escolha a curva pelo número (ou 's' para sair): ").strip().lower()
            if escolha == 's':
                print("Finalizando programa...")
                return
            try:
                idx = int(escolha)
                if 0 <= idx < len(lista_curvas):
                    pass
                else:
                    print("Número fora do intervalo. Tente novamente.")
                    continue
            except:
                print("Entrada inválida. Digite um número ou 's' para sair.")
                continue

            print(f"Curva selecionada: {lista_curvas.obter(idx).obter(0)}")
            x_teste, y_teste = 1, 0
            val = lista_curvas.obter(idx).obter(1)(x_teste, y_teste)
            print(f"Valor da curva {lista_curvas.obter(idx).obter(0)} em ({x_teste},{y_teste}): {val}")

            visual = Visualizador(lista_curvas.obter(idx))
            print("\nControles de visualização:")
            print("1 - Árvore completa")
            print("2 - Por nível (use ↑ ↓ para ajustar)")
            print("3 - Folhas na fronteira")
            print("4 - Apenas curva")
            print("Pressione a tecla correspondente para alternar modos na janela.")
            pyglet.app.run()

if __name__ == "__main__":
    main()
