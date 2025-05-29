import cNo

# *******************************************************
# ***                                                 ***
# *******************************************************
class cLSE:

# *******************************************************
# ***                                                 ***
# *******************************************************
    def __init__(self):
        self._inicio     = None
        self._numElems   = 0

# *******************************************************
# ***                                                 ***
# *******************************************************
    def getTamanho(self):
        return self._numElems

# *******************************************************
# ***                                                 ***
# *******************************************************
    def __str__(self):

        outStr = ""

        if self._inicio == None:        
            outStr += "=====================\n"
            outStr += "|   LISTA   VAZIA   |\n"
            outStr += "=====================\n"
        else:
            atual = self._inicio
            while atual is not None:
                outStr += str(atual)
                atual = atual.getProx()

        return outStr

# *******************************************************
# *** Inserção no INÍCIO                              ***
# *******************************************************
    def insereInicio(self, n):

        novo_no = cNo.cNo(n)
        novo_no.setProx(self._inicio)
        self._inicio = novo_no
        self._numElems += 1
        return True

# *******************************************************
# *** Inserção no FINAL                               ***
# *******************************************************
    def insereFim(self, n):

        novo_no = cNo.cNo(n)
        if self._inicio is None:
            self._inicio = novo_no
        else:
            atual = self._inicio
            while atual.getProx() is not None:
                atual = atual.getProx()
            atual.setProx(novo_no)
        self._numElems += 1
        return True

# *******************************************************
# *** Inserção ORDENADA                               ***
# *******************************************************
    def insereOrdenado(self, n):

        novo_no = cNo.cNo(n)

        if self._inicio is None or self._inicio.getDado() >= n:
            novo_no.setProx(self._inicio)
            self._inicio = novo_no
        else:
            atual = self._inicio
            while atual.getProx() is not None and atual.getProx().getDado() < n:
                atual = atual.getProx()
            novo_no.setProx(atual.getProx())
            atual.setProx(novo_no)

        self._numElems += 1
        return True

# *******************************************************
# *** Busca de elemento                               ***
# *******************************************************
    def buscaDado(self, n):

        atual = self._inicio
        while atual is not None:
            if atual.getDado() == n:
                return True
            atual = atual.getProx()
        return False

# *******************************************************
# *** Remoção de elemento                             ***
# *******************************************************
    def removeDado(self, n):

        atual = self._inicio
        anterior = None

        while atual is not None:
            if atual.getDado() == n:
                if anterior is None:
                    self._inicio = atual.getProx()
                else:
                    anterior.setProx(atual.getProx())
                self._numElems -= 1
                return True
            anterior = atual
            atual = atual.getProx()
        return False

# *******************************************************
# *** Teste Local                                      ***
# *******************************************************
if __name__ == '__main__':

    lista = cLSE()

    print(lista)

    lista.insereInicio(40)
    lista.insereFim(10)
    lista.insereOrdenado(25)
    lista.insereOrdenado(5)

    print("Lista após inserções:")
    print(lista)

    if lista.buscaDado(25):
        print("Busca com sucesso")
    else:
        print("Busca sem sucesso")

    if lista.removeDado(10):
        print("Remoção com sucesso")
    else:
        print("Remoção sem sucesso")

    print("Lista após remoção:")
    print(lista)
