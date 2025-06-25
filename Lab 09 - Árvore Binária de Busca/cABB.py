# #####################################################
# Classe cArvore de define uma Árvore Binária de Busca
# #####################################################

import cNo



# *******************************************************
#
# *******************************************************
class percursos:
  PRE_ORDEM   = 0
  IN_ORDEM    = 1
  POS_ORDEM   = 2
  NIVEL       = 3

class tiposNo:
  FOLHA = 0
  COMPLETO = 1
  SEMI_CHEIO = 2
  
  # *******************************************************
    


# *******************************************************
#
# *******************************************************
class cABB:
  
  # *******************************************************
  def inserir(self, dado):
    novo_no = cNo.cNo(dado)

    if self.__raiz is None:
      self.__raiz = novo_no
      self.__numNos += 1
      return True

    atual = self.__raiz
    while True:
      if dado < atual.getDado():
        if atual._cNo__filhoEsc is None:
          atual._cNo__filhoEsc = novo_no
          self.__numNos += 1
          return True
        atual = atual._cNo__filhoEsc

      elif dado > atual.getDado():
        if atual._cNo__filhoDir is None:
          atual._cNo__filhoDir = novo_no
          self.__numNos += 1
          return True
        atual = atual._cNo__filhoDir

      else:
        return False

  
# *******************************************************
  def __init__(self):
    self.__raiz = None
    self.__numNos = 0

# *******************************************************
  def getNumNos(self):
    return self.__numNos

# *******************************************************
  def percorreArvore(self, percurso=percursos.PRE_ORDEM):
    if self.__raiz is None:
      print("Árvore vazia")
      return

    print("\nPercurso:", end=" ")
    if percurso == percursos.PRE_ORDEM:
      self.__preOrdem(self.__raiz)
    elif percurso == percursos.IN_ORDEM:
      self.__inOrdem(self.__raiz)
    elif percurso == percursos.POS_ORDEM:
      self.__postOrdem(self.__raiz)
    elif percurso == percursos.NIVEL:
      self.__porNivel()
    print()  # quebra de linha final

 
# *******************************************************
  def __preOrdem(self, no):
    if no is not None:
      print(no.getDado(), end=' ')
      self.__preOrdem(no._cNo__filhoEsc)
      self.__preOrdem(no._cNo__filhoDir)


    return None 
 
# *******************************************************
  def __inOrdem(self, no):
    if no is not None:
      self.__inOrdem(no._cNo__filhoEsc)
      print(no.getDado(), end=' ')
      self.__inOrdem(no._cNo__filhoDir)

    return None 
 
# *******************************************************
  def __postOrdem(self, no):
    if no is not None:
      self.__postOrdem(no._cNo__filhoEsc)
      self.__postOrdem(no._cNo__filhoDir)
      print(no.getDado(), end=' ')

    return None 
  def __porNivel(self):
    TAM = 100  # tamanho fixo da fila
    fila = [None] * TAM
    inicio = fim = 0

    fila[fim] = self.__raiz
    fim += 1

    while inicio < fim:
      no = fila[inicio]
      inicio += 1

      if no is not None:
        print(no.getDado(), end=' ')

        if fim < TAM:
          fila[fim] = no._cNo__filhoEsc
          fim += 1
        if fim < TAM:
          fila[fim] = no._cNo__filhoDir
          fim += 1
  # *******************************************************
  def buscar(self, dado):
    atual = self.__raiz
    while atual is not None:
      if dado == atual.getDado():
        return True
      elif dado < atual.getDado():
        atual = atual._cNo__filhoEsc
      else:
        atual = atual._cNo__filhoDir
    return False
# *******************************************************

  def contarNos(self, tipo):
    def contar_rec(no):
      if no is None:
        return 0

      esquerdo = no._cNo__filhoEsc
      direito = no._cNo__filhoDir

      # conta recursivamente nos filhos
      cont_esq = contar_rec(esquerdo)
      cont_dir = contar_rec(direito)

      # verifica o tipo do nó atual
      if tipo == tiposNo.FOLHA:
        if esquerdo is None and direito is None:
          return 1 + cont_esq + cont_dir
      elif tipo == tiposNo.COMPLETO:
        if esquerdo is not None and direito is not None:
          return 1 + cont_esq + cont_dir
      elif tipo == tiposNo.SEMI_CHEIO:
        # exatamente um filho
        if (esquerdo is None) != (direito is None):
          return 1 + cont_esq + cont_dir

      # se não é o tipo pedido, só soma dos filhos
      return cont_esq + cont_dir

    return contar_rec(self.__raiz)
  # *******************************************************
  def altura(self):
    def altura_rec(no):
      if no is None:
        return -1  # altura de árvore vazia

      alt_esq = altura_rec(no._cNo__filhoEsc)
      alt_dir = altura_rec(no._cNo__filhoDir)

      if alt_esq > alt_dir:
        return alt_esq + 1
      else:
        return alt_dir + 1

    return altura_rec(self.__raiz)
  # *******************************************************
  def contarNosTotal(self):
    def contar(no):
      if no is None:
        return 0
      return 1 + contar(no._cNo__filhoEsc) + contar(no._cNo__filhoDir)
    return contar(self.__raiz)
  # *******************************************************
  def remover(self, dado):
    def remover_rec(no, dado):
      if no is None:
        return no, False

      removido = False
      if dado < no.getDado():
        no._cNo__filhoEsc, removido = remover_rec(no._cNo__filhoEsc, dado)
      elif dado > no.getDado():
        no._cNo__filhoDir, removido = remover_rec(no._cNo__filhoDir, dado)
      else:
        removido = True
        # Caso 1: nó sem filhos
        if no._cNo__filhoEsc is None and no._cNo__filhoDir is None:
          return None, True

        # Caso 2: nó com um filho
        if no._cNo__filhoEsc is None:
          return no._cNo__filhoDir, True
        elif no._cNo__filhoDir is None:
          return no._cNo__filhoEsc, True
        sucessor = no._cNo__filhoDir
        while sucessor._cNo__filhoEsc is not None:
          sucessor = sucessor._cNo__filhoEsc

        # Substituir dado do nó pelo do sucessor
        no.setDado(sucessor.getDado())

        # Remover sucessor da subárvore direita
        no._cNo__filhoDir, _ = remover_rec(no._cNo__filhoDir, sucessor.getDado())

      return no, removido

    self.__raiz, removido = remover_rec(self.__raiz, dado)
    if removido:
      self.__numNos -= 1
    return removido
  # *******************************************************
  def estruturalmenteIgual(self, outraArvore):
    def comparar(no1, no2):
      if no1 is None and no2 is None:
        return True
      if no1 is None or no2 is None:
        return False
      
      esq_igual = comparar(no1._cNo__filhoEsc, no2._cNo__filhoEsc)
      dir_igual = comparar(no1._cNo__filhoDir, no2._cNo__filhoDir)
      return esq_igual and dir_igual

    return comparar(self.__raiz, outraArvore._cABB__raiz)
  
  def identica(self, outraArvore):
    def comparar(no1, no2):
      if no1 is None and no2 is None:
        return True
      if no1 is None or no2 is None:
        return False
      if no1.getDado() != no2.getDado():
        return False

      esq = comparar(no1._cNo__filhoEsc, no2._cNo__filhoEsc)
      dir = comparar(no1._cNo__filhoDir, no2._cNo__filhoDir)
      return esq and dir

    return comparar(self.__raiz, outraArvore._cABB__raiz)
  # *******************************************************
  def espelhar(self):
    def inverter(no):
      if no is not None:
        # Troca os filhos
        temp = no._cNo__filhoEsc
        no._cNo__filhoEsc = no._cNo__filhoDir
        no._cNo__filhoDir = temp

        # Aplica recursivamente nos filhos
        inverter(no._cNo__filhoEsc)
        inverter(no._cNo__filhoDir)

    inverter(self.__raiz)
  # *******************************************************
  def imprimirArvore(self):
    def imprimir(no, prefixo="", ehEsquerda=True):
      if no is not None:
        if no._cNo__filhoDir:
          novoPrefixo = prefixo + ("│   " if ehEsquerda else "    ")
          imprimir(no._cNo__filhoDir, novoPrefixo, False)

        print(prefixo + ("└── " if ehEsquerda else "┌── ") + str(no.getDado()))

        if no._cNo__filhoEsc:
          novoPrefixo = prefixo + ("    " if ehEsquerda else "│   ")
          imprimir(no._cNo__filhoEsc, novoPrefixo, True)

    imprimir(self.__raiz)

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

# Coloque aqui seu código para testar as operações do TAD árvore binária de busca dentro do seu módulo.
    print("Teste do TAD Àrvore Binária de Busca")
    arvore = cABB()
    arvore.inserir(50)
    arvore.inserir(30)
    arvore.inserir(70)
    arvore.inserir(20)
    arvore.inserir(40)
    arvore.inserir(60)
    arvore.inserir(80)
    print("Total de nós:", arvore.getNumNos())
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        arvore.inserir(valor)
    arvore.percorreArvore(percursos.PRE_ORDEM)
    arvore.percorreArvore(percursos.IN_ORDEM)
    arvore.percorreArvore(percursos.POS_ORDEM)
    arvore.percorreArvore(percursos.NIVEL)    
    print("Busca 40:", arvore.buscar(40))  
    print("Busca 100:", arvore.buscar(100)) 
    print("Número de folhas:", arvore.contarNos(tiposNo.FOLHA))
    print("Número de nós completos:", arvore.contarNos(tiposNo.COMPLETO))
    print("Número de nós semi-cheios:", arvore.contarNos(tiposNo.SEMI_CHEIO))
    print("Altura da árvore:", arvore.altura())  
    print("Número total de nós (sem usar __numNos):", arvore.contarNosTotal())
    print("Antes da remoção (in-ordem):")
    arvore.percorreArvore(percursos.IN_ORDEM)
    print("\nRemovendo 20 (folha):", arvore.remover(20))
    print("Removendo 30 (nó com um filho):", arvore.remover(30))
    print("Removendo 50 (nó com dois filhos):", arvore.remover(50))
    print("Após remoções (in-ordem):")
    arvore.percorreArvore(percursos.IN_ORDEM)
   
    arvore1 = cABB()
    arvore2 = cABB()
    for v in [50, 30, 70, 20, 40, 60, 80]:
        arvore1.inserir(v)

    for v in [10, 5, 15, 2, 7, 12, 17]:
        arvore2.inserir(v)

    print("Estruturalmente iguais?", arvore1.estruturalmenteIgual(arvore2))  
    arvore2.remover(7)

    print("Estruturalmente iguais após remoção?", arvore1.estruturalmenteIgual(arvore2))  
    
    for v in [50, 30, 70, 20, 40, 60, 80]:
        arvore1.inserir(v)
        arvore2.inserir(v)

    print("Árvores idênticas?", arvore1.identica(arvore2))  

    arvore2.remover(40)
    print("Árvores idênticas após remoção?", arvore1.identica(arvore2)) 
    arv = cABB()
    for v in [10, 5, 15, 3, 7, 12, 18]:
        arv.inserir(v)
    print("In-ordem original:")
    arv.percorreArvore(percursos.IN_ORDEM)

    print("Espelhando a árvore...")
    arv.espelhar()

    print("In-ordem após espelhar:")
    arv.percorreArvore(percursos.IN_ORDEM)
    for v in [10, 5, 15]:
        arv.inserir(v)

    print("\nEstrutura da árvore:")
    arv.imprimirArvore()

    print("\nEspelhando...")
    arv.espelhar()

    print("\nEstrutura espelhada:")
    arv.imprimirArvore()












