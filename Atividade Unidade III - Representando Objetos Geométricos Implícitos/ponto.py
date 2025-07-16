# Classe que representa um ponto 2D com coordenadas x e y, e uma cor associada em RGB
class Ponto2D:
    # Construtor da classe: inicializa as coordenadas x e y e a cor do ponto
    # coord_x: valor da coordenada x
    # coord_y: valor da coordenada y
    # cor: tupla com valores RGB (padrão branco (255, 255, 255))
    def __init__(self, coord_x, coord_y, cor=(255,255,255)):
        self.x = coord_x            # Armazena a coordenada x do ponto
        self.y = coord_y            # Armazena a coordenada y do ponto
        self.cor = cor              # Armazena a cor do ponto (RGB)

    # Método que retorna a coordenada x do ponto
    def obter_x(self):
        return self.x               # Retorna o valor da coordenada x

    # Método que retorna a coordenada y do ponto
    def obter_y(self):
        return self.y               # Retorna o valor da coordenada y

    # Método que retorna a cor do ponto (tupla RGB)
    def obter_cor(self):
        return self.cor             # Retorna a cor associada ao ponto
