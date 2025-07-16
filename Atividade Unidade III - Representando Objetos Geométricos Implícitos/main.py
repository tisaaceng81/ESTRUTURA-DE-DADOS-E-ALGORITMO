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
from objetosGeometricos import cPonto, cRect, cCor # Importa as classes do módulo objetosGeometricos


# Define as dimensões da janela da aplicação gráfica
LARGURA_JANELA, ALTURA_JANELA = 800, 800

def gerar_faixa(inicio, fim, passo):
    """
    Função geradora que cria uma faixa de números de 'inicio' até 'fim' com
    incrementos de 'passo'. Útil para criar intervalos iterativos.
    """
    while inicio < fim:
        yield inicio
        inicio += passo

class Visualizador:
    """
    Classe responsável pela criação da janela, controle dos modos de visualização,
    desenho da árvore VDB e da curva implícita na tela.
    """
    def __init__(self, curva, largura=LARGURA_JANELA, altura=ALTURA_JANELA, profundidade=6, modo=1):
        # Inicializa atributos básicos: dimensões, curva, profundidade da árvore e modo visual
        self.largura = largura
        self.altura = altura
        self.profundidade = profundidade
        self.curva = curva

        # Cria a janela gráfica com título baseado no nome da curva
        self.janela = pyglet.window.Window(largura, altura)
        self.janela.set_caption(f"VDB - {curva.obter(0)}")

        # Define a cor de fundo da janela (branco)
        glClearColor(1,1,1,1)

        # Cria um batch para agrupar desenhos (melhora performance)
        self.batch = pyglet.graphics.Batch()
        # Estrutura para armazenar objetos desenhados (forma de vetor limitado)
        self.formas = ArrayLimitado(10000)

        # Cria a árvore VDB com profundidade e divisão especificadas
        self.arvore = EstruturaVDB(profundidade, 4) # O 4 aqui é o tamanho_espaco do retangulo raiz
        # Constroi a árvore a partir da função da curva
        self.arvore.construir_estrutura(curva.obter(1))

        # Define o modo inicial de visualização e o nível para modo por nível
        self.modo_visualizacao = modo
        self.nivel_visualizacao = 0

        # Registra os eventos da janela: desenhar e tecla pressionada
        self.janela.push_handlers(
            on_draw=self.ao_desenhar,
            on_key_press=self.ao_pressionar_tecla
        )

    def ao_desenhar(self):
        """
        Método chamado automaticamente pela biblioteca pyglet para redesenhar a janela.
        Ele limpa a tela e desenha a estrutura de acordo com o modo de visualização selecionado.
        """
        self.janela.clear()
        self.formas.resetar()  # Limpa a lista de formas armazenadas
        self.batch = pyglet.graphics.Batch()  # Reinicia o batch para novos desenhos

        # Desenha a árvore ou curva conforme o modo selecionado
        if self.modo_visualizacao == 1:
            self.desenhar_no_recursivamente(self.arvore.raiz)
        elif self.modo_visualizacao == 2:
            self.desenhar_por_nivel(self.arvore.raiz, self.nivel_visualizacao)
        elif self.modo_visualizacao == 3:
            self.desenhar_folhas_fronteira(self.arvore.raiz)
        else:
            # Se o modo for 4 (apenas curva), não desenha a estrutura da árvore
            pass # A curva é desenhada de qualquer forma após este if/elif/else

        # Garante que a curva sempre seja desenhada sobre a árvore
        self.desenhar_curva()
        # Executa o desenho de todos os objetos acumulados no batch
        self.batch.draw()

    def ao_pressionar_tecla(self, simbolo, modificadores):
        """
        Método chamado quando o usuário pressiona uma tecla.
        Modifica o modo de visualização ou ajusta o nível quando em modo por nível.
        """
        
        # Alterna entre os modos de visualização com as teclas 1 a 4
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

        # Se estiver no modo por nível, permite aumentar ou diminuir o nível com as setas ↑ ↓
        if self.modo_visualizacao == 2:
            if simbolo == key.UP:
                self.nivel_visualizacao = min(self.nivel_visualizacao + 1, self.profundidade)
                print(f"Nível selecionado: {self.nivel_visualizacao}")
            elif simbolo == key.DOWN:
                self.nivel_visualizacao = max(self.nivel_visualizacao - 1, 0)
                print(f"Nível selecionado: {self.nivel_visualizacao}")

    def desenhar_no_recursivamente(self, no):
        """
        Desenha o nó atual e seus filhos recursivamente, explorando toda a árvore.
        """
        self.desenhar_retangulo(no)
        for i in range(len(no.sub_nos)):
            self.desenhar_no_recursivamente(no.sub_nos.obter(i))

    def desenhar_por_nivel(self, no, nivel):
        """
        Desenha apenas os nós no nível especificado.
        """
        if no.nivel == nivel:
            self.desenhar_retangulo(no)
        elif no.nivel < nivel:
            for i in range(len(no.sub_nos)):
                self.desenhar_por_nivel(no.sub_nos.obter(i), nivel)

    def desenhar_folhas_fronteira(self, no):
        """
        Desenha somente as folhas que estão na fronteira da árvore.
        """
        # Verifica se o nó é uma folha (não tem subnós)
        if len(no.sub_nos) > 0:
            for i in range(len(no.sub_nos)):
                self.desenhar_folhas_fronteira(no.sub_nos.obter(i))
        else:
            self.desenhar_retangulo(no)

    def desenhar_retangulo(self, no):
        """
        Desenha um retângulo colorido representando o nó da árvore,
        usando uma paleta de cores para diferenciar os níveis.
        """
        escala_x = self.largura / self.arvore.tamanho_espaco  # Ajusta escala horizontal para coordenadas do nó
        escala_y = self.altura / self.arvore.tamanho_espaco   # Ajusta escala vertical para coordenadas do nó

        # Obtém as coordenadas e dimensões do retângulo do nó
        x_base = no.retangulo.getPtoBase().getX()
        y_base = no.retangulo.getPtoBase().getY()
        largura_ret = no.retangulo.getWidth()
        altura_ret = no.retangulo.getHeight()

        # Converte as coordenadas do nó para coordenadas da janela
        # O espaço vai de -tamanho_espaco/2 a tamanho_espaco/2. Para mapear para 0 a largura/altura da janela,
        # adicionamos tamanho_espaco/2 antes de multiplicar pela escala.
        x = int((x_base + self.arvore.tamanho_espaco / 2) * escala_x)
        y = int((y_base + self.arvore.tamanho_espaco / 2) * escala_y)
        largura = int(largura_ret * escala_x)
        altura = int(altura_ret * escala_y)

        # Paleta de cores fixa para os níveis da árvore
        paleta_cores = ArrayLimitado(7)
        paleta_cores.adicionar(0, (255, 0, 0))       # Vermelho
        paleta_cores.adicionar(1, (0, 255, 0))       # Verde
        paleta_cores.adicionar(2, (0, 0, 255))       # Azul
        paleta_cores.adicionar(3, (255, 165, 0))     # Laranja
        paleta_cores.adicionar(4, (128, 0, 128))     # Roxo
        paleta_cores.adicionar(5, (0, 255, 255))     # Ciano
        paleta_cores.adicionar(6, (255, 192, 203))   # Rosa

        # Obtém a cor como uma tupla RGB
        cor_rgb = paleta_cores.obter(no.nivel % 7)
        # No_vdb armazena a cor como cCor, mas para shapes.Rectangle precisamos de uma tupla
        # no.cor.setCor(*cor_rgb) # Se você quisesse atribuir a cor ao nó, mas não é necessário aqui
        
        # Cria o retângulo que representa o nó na tela
        retangulo = shapes.Rectangle(x, y, largura, altura, color=cor_rgb, batch=self.batch)
        retangulo.opacity = 120  # Transparência para melhor visualização
        self.formas.adicionar(len(self.formas), retangulo)  # Armazena o retângulo para controle

        # Desenha as bordas do retângulo usando linhas pretas
        linhas = ArrayLimitado(4)
        linhas.adicionar(len(linhas), shapes.Line(x, y, x+largura, y, width=1, color=(0,0,0), batch=self.batch))
        linhas.adicionar(len(linhas), shapes.Line(x+largura, y, x+largura, y+altura, width=1, color=(0,0,0), batch=self.batch))
        linhas.adicionar(len(linhas), shapes.Line(x+largura, y+altura, x, y+altura, width=1, color=(0,0,0), batch=self.batch))
        linhas.adicionar(len(linhas), shapes.Line(x, y+altura, x, y, width=1, color=(0,0,0), batch=self.batch))

        # Adiciona as linhas à lista de formas para serem desenhadas
        for i in range(len(linhas)):
            self.formas.adicionar(len(self.formas), linhas.obter(i))

    def desenhar_curva(self):
        """
        Desenha a curva implícita na janela verificando pontos próximos de zero
        na função da curva, usando um passo fixo para varrer o espaço.
        """
        escala_x = self.largura / self.arvore.tamanho_espaco  # Escala horizontal
        escala_y = self.altura / self.arvore.tamanho_espaco   # Escala vertical
        passo = 0.01                 # Incremento para varredura dos pontos
        
        # O espaço de trabalho é de -tamanho_espaco/2 a tamanho_espaco/2 em X e Y
        x_min = -self.arvore.tamanho_espaco / 2
        x_max = self.arvore.tamanho_espaco / 2
        y_min = -self.arvore.tamanho_espaco / 2
        y_max = self.arvore.tamanho_espaco / 2
        
        x_atual = x_min
        while x_atual < x_max:
            y_atual = y_min
            while y_atual < y_max:
                # Verifica se o valor da função da curva está próximo de zero (contorno)
                if abs(self.curva.obter(1)(x_atual, y_atual)) < 0.01:
                    # Calcula posição na janela para desenhar o ponto
                    # Mapeia de [-tamanho_espaco/2, tamanho_espaco/2] para [0, largura/altura] da janela
                    px = int((x_atual - x_min) * escala_x)
                    py = int((y_atual - y_min) * escala_y)
                    # Desenha um pequeno círculo preto representando o ponto da curva
                    ponto = shapes.Circle(px, py, 1, color=(0,0,0), batch=self.batch)
                    self.formas.adicionar(len(self.formas), ponto)
                y_atual += passo
            x_atual += passo

def main():
    """
    Função principal que controla a execução do programa.
    Permite passar argumentos para escolher curva e modo,
    ou exibe menu interativo para o usuário escolher.
    """
    argumentos = sys.argv[1:]
    if argumentos:
        # Tenta interpretar o primeiro argumento como índice da curva
        try:
            idx = int(argumentos[0])
            if not (0 <= idx < len(lista_curvas)):
                print(f"Índice inválido. Use valores entre 0 e {len(lista_curvas)-1}")
                return
        except:
            print("O primeiro argumento deve ser um número inteiro correspondente à curva.")
            return

        # Define modo de visualização, pode ser passado como segundo argumento
        modo_vis = 1
        if len(argumentos) > 1:
            try:
                modo_vis = int(argumentos[1])
                if modo_vis not in [1, 2, 3, 4]:
                    print("Modo de visualização inválido. Usando modo padrão 1.")
                    modo_vis = 1
            except:
                print("Segundo argumento deve ser um número de modo (1 a 4). Usando modo padrão 1.")

        # Exibe informações da curva selecionada e valor em ponto teste
        print(f"Curva selecionada: {lista_curvas.obter(idx).obter(0)}")
        
        # Crie um cPonto para o teste, embora as coordenadas x, y sejam suficientes para a função da curva.
        # A classe cPonto é mais relevante para o desenho e estrutura da árvore.
        # x_teste, y_teste = 1, 0 # Pode continuar assim se a função da curva espera apenas x, y
        ponto_teste = cPonto(1, 0) # Ou usar cPonto diretamente se a função da curva esperasse um Ponto2D
        x_teste, y_teste = ponto_teste.getX(), ponto_teste.getY() # Acessando as coordenadas do cPonto

        val = lista_curvas.obter(idx).obter(1)(x_teste, y_teste)
        print(f"Valor da curva {lista_curvas.obter(idx).obter(0)} em ({x_teste},{y_teste}): {val}")

        # Cria o visualizador e inicia a janela
        visual = Visualizador(lista_curvas.obter(idx), modo=modo_vis)
        print("Janela aberta. Feche para encerrar.")
        pyglet.app.run()

    else:
        # Menu interativo para seleção de curvas
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

            # Valida a entrada do usuário
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

            # Exibe detalhes da curva escolhida
            print(f"Curva selecionada: {lista_curvas.obter(idx).obter(0)}")

            ponto_teste = cPonto(1, 0) # Usando cPonto
            x_teste, y_teste = ponto_teste.getX(), ponto_teste.getY() # Acessando as coordenadas do cPonto

            val = lista_curvas.obter(idx).obter(1)(x_teste, y_teste)
            print(f"Valor da curva {lista_curvas.obter(idx).obter(0)} em ({x_teste},{y_teste}): {val}")

            # Cria e mostra a janela com a curva selecionada
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