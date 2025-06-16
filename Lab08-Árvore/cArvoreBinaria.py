# ##################################################
# Classe cArvoreBinária
# ##################################################

import cNo

class percursos:
  PRE_ORDEM   = 0
  IN_ORDEM    = 1
  POST_ORDEM  = 2

class cArvoreBinaria:
  
  chave = 0

  # =====================================================
  # SEÇÃO: Construtor e Métodos Básicos
  # =====================================================
  def __init__(self, n):
    self.__raiz    = None
    self.__numNos = n
    cArvoreBinaria.chave = 0
    self.__raiz    = self.__MontaAB(n, 0)

  def getNumNos(self):
    return self.__numNos

  def getRaiz(self):
    return self.__raiz

  # =====================================================
  # SEÇÃO: Construção da Árvore
  # =====================================================
  def __MontaAB(self, n, nivel):
    if n <= 0:
      return None
    cArvoreBinaria.chave += 1
    no = cNo.cNo(cArvoreBinaria.chave, nivel)
    n_restantes = n - 1
    n_esq = n_restantes // 2
    n_dir = n_restantes - n_esq
    no.setFilhoEsq(self.__MontaAB(n_esq, nivel + 1))
    no.setFilhoDir(self.__MontaAB(n_dir, nivel + 1))
    return no

  # =====================================================
  # SEÇÃO: Percursos
  # =====================================================
  def percorreArvore(self, percurso=percursos.PRE_ORDEM):
    if percurso == percursos.PRE_ORDEM:
      self.__preOrdem(self.__raiz)
    elif percurso == percursos.IN_ORDEM:
      self.__inOrdem(self.__raiz)
    elif percurso == percursos.POST_ORDEM:
      self.__postOrdem(self.__raiz)
  
  def __preOrdem(self, raiz):
    if raiz is None:
      return
    print(f" {raiz.getDado()}", end="")
    self.__preOrdem(raiz.getFilhoEsq())
    self.__preOrdem(raiz.getFilhoDir())
  
  def __inOrdem(self, raiz):
    if raiz is None:
      return
    self.__inOrdem(raiz.getFilhoEsq())
    print(f" {raiz.getDado()}", end="")
    self.__inOrdem(raiz.getFilhoDir())

  def __postOrdem(self, raiz):
    if raiz is None:
      return
    self.__postOrdem(raiz.getFilhoEsq())
    self.__postOrdem(raiz.getFilhoDir())
    print(f" {raiz.getDado()}", end="")
    
  # =====================================================
  # SEÇÃO: Cálculo de Altura
  # =====================================================
  def getAltura(self):
    return self.__calculaAltura(self.__raiz)

  def __calculaAltura(self, no):
    if no is None:
      return -1 
    altura_esq = self.__calculaAltura(no.getFilhoEsq())
    altura_dir = self.__calculaAltura(no.getFilhoDir())
    return 1 + max(altura_esq, altura_dir)

  # =====================================================
  # SEÇÃO: Contagem de Nós por Tipo
  # =====================================================
  def contaTiposDeNos(self):
    if self.__raiz is None:
      return (0, 0, 0)
    return self.__contaTipos(self.__raiz)

  def __contaTipos(self, no):
    if no is None:
      return (0, 0, 0)
    cont_esq = self.__contaTipos(no.getFilhoEsq())
    cont_dir = self.__contaTipos(no.getFilhoDir())
    folhas_aqui, completos_aqui, semi_aqui = 0, 0, 0
    filho_esq = no.getFilhoEsq()
    filho_dir = no.getFilhoDir()
    if filho_esq is None and filho_dir is None:
      folhas_aqui = 1
    elif filho_esq is not None and filho_dir is not None:
      completos_aqui = 1
    else:
      semi_aqui = 1
    total_folhas = folhas_aqui + cont_esq[0] + cont_dir[0]
    total_completos = completos_aqui + cont_esq[1] + cont_dir[1]
    total_semi = semi_aqui + cont_esq[2] + cont_dir[2]
    return (total_folhas, total_completos, total_semi)

  # =====================================================
  # SEÇÃO: Contagem Total de Nós (Recursivo)
  # =====================================================
  def getNumNosTotal(self):
    return self.__contaNos(self.__raiz)
  
  def __contaNos(self, no):
    if no is None:
      return 0
    return 1 + self.__contaNos(no.getFilhoEsq()) + self.__contaNos(no.getFilhoDir())

  # =====================================================
  # SEÇÃO: Comparação de Árvores
  # =====================================================
  def saoEstruturalmenteIdenticas(self, outra_arvore):
    return self.__comparaEstrutura(self.getRaiz(), outra_arvore.getRaiz())

  def __comparaEstrutura(self, no1, no2):
    if no1 is None and no2 is None:
      return True
    if no1 is None or no2 is None:
      return False
    return (self.__comparaEstrutura(no1.getFilhoEsq(), no2.getFilhoEsq()) and
            self.__comparaEstrutura(no1.getFilhoDir(), no2.getFilhoDir()))

  def saoIdenticas(self, outra_arvore):
    return self.__comparaTudo(self.getRaiz(), outra_arvore.getRaiz())

  def __comparaTudo(self, no1, no2):
    if no1 is None and no2 is None:
      return True
    if no1 is None or no2 is None:
      return False
    return ((no1.getDado() == no2.getDado()) and
            self.__comparaTudo(no1.getFilhoEsq(), no2.getFilhoEsq()) and
            self.__comparaTudo(no1.getFilhoDir(), no2.getFilhoDir()))