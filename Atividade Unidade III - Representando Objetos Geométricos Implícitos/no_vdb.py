# Módulo: no_vdb.py
# Representa um nó da árvore VDB que subdivide o espaço se houver interseção com uma curva.
# Não utiliza listas nativas. Usa ArrayLimitado para conter os subnós.

from vetor import ArrayLimitado  # Importa o vetor fixo para conter subnós (sem listas nativas)

class NodoVDB:
    def __init__(self, x_inicial, y_inicial, largura, altura, nivel_atual):
        # Coordenadas do canto inferior esquerdo do retângulo
        self.x = x_inicial
        self.y = y_inicial

        # Dimensões do retângulo
        self.largura = largura
        self.altura = altura

        # Nível atual da subdivisão
        self.nivel = nivel_atual

        # Estrutura para armazenar os subnós (filhos)
        self.sub_nos = ArrayLimitado(4)  # Inicialmente vazio

        # Cor padrão do retângulo (usada para visualização)
        self.cor = (100, 100, 100)

    def verifica_objeto(self, funcao):
        """
        Verifica se a curva interage com o retângulo.
        Isso é feito avaliando os valores da função nos quatro cantos e no centro.
        """
        # Define os pontos a avaliar usando vetores
        pontos_x = ArrayLimitado(5)
        pontos_y = ArrayLimitado(5)

        # Canto inferior esquerdo
        pontos_x.adicionar(len(pontos_x), self.x)
        pontos_y.adicionar(len(pontos_y), self.y)

        # Canto inferior direito
        pontos_x.adicionar(len(pontos_x), self.x + self.largura)
        pontos_y.adicionar(len(pontos_y), self.y)

        # Canto superior esquerdo
        pontos_x.adicionar(len(pontos_x), self.x)
        pontos_y.adicionar(len(pontos_y), self.y + self.altura)

        # Canto superior direito
        pontos_x.adicionar(len(pontos_x), self.x + self.largura)
        pontos_y.adicionar(len(pontos_y), self.y + self.altura)

        # Centro
        pontos_x.adicionar(len(pontos_x), self.x + self.largura / 2)
        pontos_y.adicionar(len(pontos_y), self.y + self.altura / 2)

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

        # Calcula metade das dimensões
        metade_larg = self.largura / 2
        metade_alt = self.altura / 2

        # Cria os 4 subnós e os adiciona ao vetor
        self.sub_nos.adicionar(len(self.sub_nos), NodoVDB(self.x, self.y, metade_larg, metade_alt, self.nivel + 1))
        self.sub_nos.adicionar(len(self.sub_nos), NodoVDB(self.x + metade_larg, self.y, metade_larg, metade_alt, self.nivel + 1))
        self.sub_nos.adicionar(len(self.sub_nos), NodoVDB(self.x, self.y + metade_alt, metade_larg, metade_alt, self.nivel + 1))
        self.sub_nos.adicionar(len(self.sub_nos), NodoVDB(self.x + metade_larg, self.y + metade_alt, metade_larg, metade_alt, self.nivel + 1))

        # Aplica recursivamente nos subnós
        for i in range(len(self.sub_nos)):
            self.sub_nos.obter(i).dividir(profundidade_limite, funcao)
