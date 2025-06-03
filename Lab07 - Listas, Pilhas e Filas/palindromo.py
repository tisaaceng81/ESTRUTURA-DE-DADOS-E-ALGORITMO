from listaencad import ListaEncadeada
from no import No
class Pilha:
    def __init__(self):
        self.itens = ListaEncadeada()

    def push(self, valor):
        novo = No(valor)
        novo.proximo = self.itens.inicio
        self.itens.inicio = novo

    def pop(self):
        if self.itens.inicio is None:
            return None
        valor = self.itens.inicio.dado
        self.itens.inicio = self.itens.inicio.proximo
        return valor

    def esta_vazia(self):
        return self.itens.inicio is None


def eh_palindromo(palavra):
    pilha = Pilha()
    for c in palavra:
        pilha.push(c)

    for c in palavra:
        if c != pilha.pop():
            return False
    return True
if __name__ == "__main__":
    palavra = input("Digite uma palavra para verificar se é palíndromo: ").strip().lower()
    if eh_palindromo(palavra):
        print(f'"{palavra}" é um palíndromo.')
    else:
        print(f'"{palavra}" não é um palíndromo.')
