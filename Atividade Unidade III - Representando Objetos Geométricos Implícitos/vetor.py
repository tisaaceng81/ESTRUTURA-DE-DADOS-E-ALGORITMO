class ArrayLimitado:
    def __init__(self, max_tam):
        # Inicializa um array com tamanho máximo fixo, elementos None inicialmente
        self.max_tam = max_tam
        self.elementos = [None] * max_tam
        self.atual_tam = 0  # Quantidade atual de elementos válidos

    def adicionar(self, indice, valor):
        # Insere valor na posição indice, deslocando elementos para frente
        if self.atual_tam >= self.max_tam:
            raise OverflowError("Array está cheio")  # Não permite ultrapassar capacidade
        if indice < 0 or indice > self.atual_tam:
            raise IndexError("Índice fora do permitido")  # Checa limites válidos para inserção
        
        # Desloca elementos para frente a partir do fim até o índice onde será inserido
        for i in range(self.atual_tam, indice, -1):
            self.elementos[i] = self.elementos[i-1]
        
        # Insere o valor no índice
        self.elementos[indice] = valor
        self.atual_tam += 1  # Incrementa tamanho atual

    def resetar(self):
        # Limpa o array definindo os elementos válidos para None e tamanho zero
        for i in range(self.atual_tam):
            self.elementos[i] = None
        self.atual_tam = 0

    def obter(self, indice):
        # Retorna o elemento no índice especificado, checando limites
        if indice < 0 or indice >= self.atual_tam:
            raise IndexError("Índice fora do permitido")
        return self.elementos[indice]

    def __len__(self):
        # Retorna o tamanho atual (número de elementos válidos)
        return self.atual_tam

    def __iter__(self):
        # Permite iterar sobre os elementos válidos do array
        for i in range(self.atual_tam):
            yield self.elementos[i]
