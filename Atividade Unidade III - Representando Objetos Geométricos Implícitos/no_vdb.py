# Módulo: no_vdb.py
# Representa um nó da árvore VDB que subdivide o espaço se houver interseção com uma curva.
# Não utiliza listas nativas. Usa ArrayLimitado para conter os subnós.

from vetor import ArrayLimitado  # Importa o vetor fixo para conter subnós (sem listas nativas)
from objetosGeometricos import cPonto, cRect, cCor # Importa as classes do módulo objetosGeometricos

class NodoVDB:
    def __init__(self, x_inicial, y_inicial, largura, altura, nivel_atual):
        # Coordenadas do canto inferior esquerdo do retângulo
        # self.x = x_inicial # REMOVER
        # self.y = y_inicial # REMOVER

        # Dimensões do retângulo
        # self.largura = largura # REMOVER
        # self.altura = altura   # REMOVER

        # Agora, o nó VDB armazena um objeto cRect
        self.retangulo = cRect(cPonto(x_inicial, y_inicial), largura, altura) # Usando cPonto e cRect

        # Nível atual da subdivisão
        self.nivel = nivel_atual

        # Estrutura para armazenar os subnós (filhos)
        self.sub_nos = ArrayLimitado(4)  # Inicialmente vazio

        # Cor padrão do retângulo (usada para visualização) - pode ser removida se a cor for definida no desenho
        self.cor = cCor(100, 100, 100) # Usando cCor

    # Adicionar métodos get para acesso às propriedades do retângulo, ou acessar diretamente via self.retangulo
    def get_x(self):
        return self.retangulo.getPtoBase().getX()

    def get_y(self):
        return self.retangulo.getPtoBase().getY()

    def get_largura(self):
        return self.retangulo.getWidth()

    def get_altura(self):
        return self.retangulo.getHeight()

    def verifica_objeto(self, funcao):
        """
        Verifica se a curva interage com o retângulo.
        Isso é feito avaliando os valores da função nos quatro cantos e no centro.
        """
        # Define os pontos a avaliar usando vetores
        pontos_x = ArrayLimitado(5)
        pontos_y = ArrayLimitado(5)

        # Usar as propriedades do cRect
        x_base = self.retangulo.getPtoBase().getX()
        y_base = self.retangulo.getPtoBase().getY()
        larg = self.retangulo.getWidth()
        alt = self.retangulo.getHeight()

        # Canto inferior esquerdo
        pontos_x.adicionar(len(pontos_x), x_base)
        pontos_y.adicionar(len(pontos_y), y_base)

        # Canto inferior direito
        pontos_x.adicionar(len(pontos_x), x_base + larg)
        pontos_y.adicionar(len(pontos_y), y_base)

        # Canto superior esquerdo
        pontos_x.adicionar(len(pontos_x), x_base)
        pontos_y.adicionar(len(pontos_y), y_base + alt)

        # Canto superior direito
        pontos_x.adicionar(len(pontos_x), x_base + larg)
        pontos_y.adicionar(len(pontos_y), y_base + alt)

        # Centro
        pontos_x.adicionar(len(pontos_x), x_base + larg / 2)
        pontos_y.adicionar(len(pontos_y), y_base + alt / 2)

        tem_negativo = False
        tem_positivo = False

        for i in range(len(pontos_x)):
            valor = funcao(pontos_x.obter(i), pontos_y.obter(i))
            if valor <= 0:
                tem_negativo = True
            if valor >= 0:
                tem_positivo = True

        return tem_negativo and tem_positivo

    def dividir(self, profundidade_limite, funcao):
        """
        Subdivide o retângulo em quatro sub-regiões, se ele estiver dentro da curva.
        A subdivisão ocorre até um limite de profundidade.
        """
        if self.nivel >= profundidade_limite:
            return

        if not self.verifica_objeto(funcao):
            return

        # Usar as propriedades do cRect
        x_base = self.retangulo.getPtoBase().getX()
        y_base = self.retangulo.getPtoBase().getY()
        larg = self.retangulo.getWidth()
        alt = self.retangulo.getHeight()

        # Calcula metade das dimensões
        metade_larg = larg / 2
        metade_alt = alt / 2

        # Cria os 4 subnós e os adiciona ao vetor
        self.sub_nos.adicionar(len(self.sub_nos), NodoVDB(x_base, y_base, metade_larg, metade_alt, self.nivel + 1))
        self.sub_nos.adicionar(len(self.sub_nos), NodoVDB(x_base + metade_larg, y_base, metade_larg, metade_alt, self.nivel + 1))
        self.sub_nos.adicionar(len(self.sub_nos), NodoVDB(x_base, y_base + metade_alt, metade_larg, metade_alt, self.nivel + 1))
        self.sub_nos.adicionar(len(self.sub_nos), NodoVDB(x_base + metade_larg, y_base + metade_alt, metade_larg, metade_alt, self.nivel + 1))

        # Aplica recursivamente nos subnós
        for i in range(len(self.sub_nos)):
            self.sub_nos.obter(i).dividir(profundidade_limite, funcao)