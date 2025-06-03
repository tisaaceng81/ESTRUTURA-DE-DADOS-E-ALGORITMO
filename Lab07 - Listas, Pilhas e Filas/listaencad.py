from no import No

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir_fim(self, valor):
        novo = No(valor)
        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

    def exibir(self):
        atual = self.inicio
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("None")

    def buscar_ocorrencias(self, chave):
        atual = self.inicio
        cont = 0
        while atual:
            if atual.dado == chave:
                cont += 1
            atual = atual.proximo
        return cont

    def remover_todas_ocorrencias(self, chave):
        while self.inicio and self.inicio.dado == chave:
            self.inicio = self.inicio.proximo
        atual = self.inicio
        while atual and atual.proximo:
            if atual.proximo.dado == chave:
                atual.proximo = atual.proximo.proximo
            else:
                atual = atual.proximo

    def juntar_listas(self, outra):
        if self.inicio is None:
            self.inicio = outra.inicio
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = outra.inicio
        outra.inicio = None

    def mesclar_listas(self, outra, ordenada=False):
        if ordenada:
            dummy = No(0)
            tail = dummy
            a = self.inicio
            b = outra.inicio
            while a and b:
                if a.dado <= b.dado:
                    tail.proximo = a
                    a = a.proximo
                else:
                    tail.proximo = b
                    b = b.proximo
                tail = tail.proximo
            tail.proximo = a if a else b
            self.inicio = dummy.proximo
        else:
            a = self.inicio
            b = outra.inicio
            dummy = No(0)
            tail = dummy
            while a or b:
                if a:
                    tail.proximo = a
                    a = a.proximo
                    tail = tail.proximo
                    tail.proximo = None
                if b:
                    tail.proximo = b
                    b = b.proximo
                    tail = tail.proximo
                    tail.proximo = None
            self.inicio = dummy.proximo
        outra.inicio = None

    def comparar_listas(self, outra):
        a = self.inicio
        b = outra.inicio
        while a and b:
            if a.dado != b.dado:
                return False
            a = a.proximo
            b = b.proximo
        return a is None and b is None

if __name__ == "__main__":
    l1 = ListaEncadeada()
    l2 = ListaEncadeada()
    for v in [1, 2, 3, 2, 4]:
        l1.inserir_fim(v)
    print("Lista 1:")
    l1.exibir()

    print("Ocorrências de 2:", l1.buscar_ocorrencias(2))

    l1.remover_todas_ocorrencias(2)
    print("Após remover 2:")
    l1.exibir()

    for v in [5, 6]:
        l2.inserir_fim(v)

    l1.juntar_listas(l2)
    print("Após junção com l2:")
    l1.exibir()
    print("Lista 2 agora:")
    l2.exibir()
