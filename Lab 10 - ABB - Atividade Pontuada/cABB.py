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
#
# *******************************************************

class cABB:
  
# *******************************************************

  def __init__(self):
    self.__raiz = None
    self.__numNos = 0

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

  def getNumNos(self):
    return self.__numNos
  
# *******************************************************

  def percorreArvore(self, percurso=percursos.PRE_ORDEM):
    if self.__raiz is None:
      print("\nÁrvore vazia")
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
    print()

# *******************************************************
  
  def __preOrdem(self, no):
    if no is not None:
      print(no.getDado(), end=' ')
      self.__preOrdem(no._cNo__filhoEsc)
      self.__preOrdem(no._cNo__filhoDir)
      
# *******************************************************
  
  def __inOrdem(self, no):
    if no is not None:
      self.__inOrdem(no._cNo__filhoEsc)
      print(no.getDado(), end=' ')
      self.__inOrdem(no._cNo__filhoDir)
      
# *******************************************************

  def __postOrdem(self, no):
    if no is not None:
      self.__postOrdem(no._cNo__filhoEsc)
      self.__postOrdem(no._cNo__filhoDir)
      print(no.getDado(), end=' ')

  def __porNivel(self):
    TAM = 100
    fila = [None] * TAM
    ini = fim = 0
    if self.__raiz is not None:
      fila[fim] = self.__raiz
      fim += 1
    while ini < fim:
      no = fila[ini]
      ini += 1
      if no is not None:
        print(no.getDado(), end=' ')
        if fim < TAM:
          fila[fim] = no._cNo__filhoEsc
          fim += 1
        if fim < TAM:
          fila[fim] = no._cNo__filhoDir
          fim += 1

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

  def contarNos(self, tipo):
    def contar_rec(no):
      if no is None:
        return 0
      esq = no._cNo__filhoEsc
      dir = no._cNo__filhoDir
      cont_esq = contar_rec(esq)
      cont_dir = contar_rec(dir)
      if tipo == tiposNo.FOLHA and esq is None and dir is None:
        return 1 + cont_esq + cont_dir
      if tipo == tiposNo.COMPLETO and esq is not None and dir is not None:
        return 1 + cont_esq + cont_dir
      if tipo == tiposNo.SEMI_CHEIO and (esq is None) != (dir is None):
        return 1 + cont_esq + cont_dir
      return cont_esq + cont_dir
    return contar_rec(self.__raiz)

  def altura(self):
    def altura_rec(no):
      if no is None:
        return -1
      a = altura_rec(no._cNo__filhoEsc)
      b = altura_rec(no._cNo__filhoDir)
      return 1 + (a if a > b else b)
    return altura_rec(self.__raiz)

  def contarNosTotal(self):
    def contar(no):
      if no is None:
        return 0
      return 1 + contar(no._cNo__filhoEsc) + contar(no._cNo__filhoDir)
    return contar(self.__raiz)

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
        if no._cNo__filhoEsc is None and no._cNo__filhoDir is None:
          return None, True
        if no._cNo__filhoEsc is None:
          return no._cNo__filhoDir, True
        if no._cNo__filhoDir is None:
          return no._cNo__filhoEsc, True
        suc = no._cNo__filhoDir
        while suc._cNo__filhoEsc is not None:
          suc = suc._cNo__filhoEsc
        no.setDado(suc.getDado())
        no._cNo__filhoDir, _ = remover_rec(no._cNo__filhoDir, suc.getDado())
      return no, removido
    self.__raiz, ok = remover_rec(self.__raiz, dado)
    if ok:
      self.__numNos -= 1
    return ok

  def estruturalmenteIgual(self, outra):
    def comparar(no1, no2):
      if no1 is None and no2 is None:
        return True
      if no1 is None or no2 is None:
        return False
      return comparar(no1._cNo__filhoEsc, no2._cNo__filhoEsc) and \
             comparar(no1._cNo__filhoDir, no2._cNo__filhoDir)
    return comparar(self.__raiz, outra._cABB__raiz)

  def identica(self, outra):
    def comparar(no1, no2):
      if no1 is None and no2 is None:
        return True
      if no1 is None or no2 is None:
        return False
      if no1.getDado() != no2.getDado():
        return False
      return comparar(no1._cNo__filhoEsc, no2._cNo__filhoEsc) and \
             comparar(no1._cNo__filhoDir, no2._cNo__filhoDir)
    return comparar(self.__raiz, outra._cABB__raiz)

  def espelhar(self):
    def inverter(no):
      if no:
        no._cNo__filhoEsc, no._cNo__filhoDir = no._cNo__filhoDir, no._cNo__filhoEsc
        inverter(no._cNo__filhoEsc)
        inverter(no._cNo__filhoDir)
    inverter(self.__raiz)

  def imprimirArvore(self):
    def imprimir(no, prefixo="", esquerda=True):
      if no:
        if no._cNo__filhoDir:
          novo = prefixo + ("│   " if esquerda else "    ")
          imprimir(no._cNo__filhoDir, novo, False)
        alt = self.alturaNo(no)
        print(prefixo + ("└── " if esquerda else "┌── ") + f"{no.getDado()} (h={alt})")
        if no._cNo__filhoEsc:
          novo = prefixo + ("    " if esquerda else "│   ")
          imprimir(no._cNo__filhoEsc, novo, True)
    imprimir(self.__raiz)

  def alturaNo(self, no):
    if no is None:
      return -1
    a = self.alturaNo(no._cNo__filhoEsc)
    b = self.alturaNo(no._cNo__filhoDir)
    return 1 + (a if a > b else b)
  def gerarEspelhada(self):
    nova = cABB()
    
    def copiarEspelhado(no):
      if no is None:
        return None
      novo = cNo.cNo(no.getDado())
      novo._cNo__filhoDir = copiarEspelhado(no._cNo__filhoEsc)
      novo._cNo__filhoEsc = copiarEspelhado(no._cNo__filhoDir)
      return novo

    nova._cABB__raiz = copiarEspelhado(self.__raiz)
    nova._cABB__numNos = self.__numNos
    return nova

  def listarIntervalo(self, minimo, maximo):
      class NoLista:
          def __init__(self, valor):
              self.valor = valor
              self.prox = None
      self.__listaInicio = None
      self.__listaFim = None

      def adicionar(valor):
          novo = NoLista(valor)
          if self.__listaInicio is None:
              self.__listaInicio = novo
              self.__listaFim = novo
          else:
              self.__listaFim.prox = novo
              self.__listaFim = novo

      def percorrer(no):
          if no is None:
              return
          if no.getDado() > minimo:
              percorrer(no._cNo__filhoEsc)
          if minimo <= no.getDado() <= maximo:
              adicionar(no.getDado())
          if no.getDado() < maximo:
              percorrer(no._cNo__filhoDir)

      percorrer(self.__raiz)
      return self.__listaInicio
    
  def removerIntervalo(self, minimo, maximo):
      def remover_rec(no):
          if no is None:
              return None
          # Primeiro processa esquerda e direita
          no._cNo__filhoEsc = remover_rec(no._cNo__filhoEsc)
          no._cNo__filhoDir = remover_rec(no._cNo__filhoDir)
          # Depois verifica se precisa remover este nó
          if minimo <= no.getDado() <= maximo:
              self.__numNos -= 1
              if no._cNo__filhoEsc is None:
                  return no._cNo__filhoDir
              if no._cNo__filhoDir is None:
                  return no._cNo__filhoEsc
              # Substitui pelo menor valor da subárvore direita
              sucessor = no._cNo__filhoDir
              while sucessor._cNo__filhoEsc is not None:
                  sucessor = sucessor._cNo__filhoEsc
              no.setDado(sucessor.getDado())
              no._cNo__filhoDir = self.__removerAux(no._cNo__filhoDir, sucessor.getDado())
          return no

      self.__raiz = remover_rec(self.__raiz)

  def __removerAux(self, no, dado):
      if no is None:
          return None
      if dado < no.getDado():
          no._cNo__filhoEsc = self.__removerAux(no._cNo__filhoEsc, dado)
      elif dado > no.getDado():
          no._cNo__filhoDir = self.__removerAux(no._cNo__filhoDir, dado)
      else:
          if no._cNo__filhoEsc is None:
              return no._cNo__filhoDir
          elif no._cNo__filhoDir is None:
              return no._cNo__filhoEsc
          temp = no._cNo__filhoDir
          while temp._cNo__filhoEsc is not None:
              temp = temp._cNo__filhoEsc
          no.setDado(temp.getDado())
          no._cNo__filhoDir = self.__removerAux(no._cNo__filhoDir, temp.getDado())
      return no


# ==================== TESTE ============================
# *******************************************************
# *** Teste do TAD Árvore Binária de Busca            ***
# *******************************************************
if __name__ == '__main__':

  print("Teste do TAD Árvore Binária de Busca")
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
  
  print("\n===== Gerando árvore espelhada SEM alterar original =====")
  arvEspelhada = arv.gerarEspelhada()
  print("\nÁrvore original (IN-ORDEM):")
  arv.percorreArvore(percursos.IN_ORDEM)

  print("\nÁrvore espelhada (IN-ORDEM):")
  arvEspelhada.percorreArvore(percursos.IN_ORDEM)

  print("\nVisual da árvore espelhada:")
  arvEspelhada.imprimirArvore()
  print("\n=== Listar valores no intervalo [10, 60] ===")
  resultado = arvore.listarIntervalo(10, 60)
  atual = resultado
  while atual:
    print(atual.valor, end=' ')
    atual = atual.prox
  print()
  print("\n=== TESTE REMOVER INTERVALO [35, 65] ===")
  arvTeste = cABB()
  for v in [50, 30, 70, 20, 40, 60, 80]:
      arvTeste.inserir(v)

  print("Árvore antes (IN-ORDEM):")
  arvTeste.percorreArvore(percursos.IN_ORDEM)

  print("Removendo intervalo [35, 65]...")
  arvTeste.removerIntervalo(35, 65)

  print("Árvore depois (IN-ORDEM):")
  arvTeste.percorreArvore(percursos.IN_ORDEM)

