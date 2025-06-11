# ##################################################
# Classe cArvoreBinária
# ##################################################

import cNo

# *******************************************************
#
# *******************************************************
class percursos:
  PRE_ORDEM   = 0
  IN_ORDEM    = 1
  POST_ORDEM  = 2

# *******************************************************
#
# *******************************************************
class cArvoreBinaria:
  
  chave = 0
def __init__(self, n):
    self.__raiz   = None
    self.__numNos = 0
    self.__raiz   = self.__MontaAB(n)

# *******************************************************
  
# *******************************************************
def getNumNos(self):
    return self.__numNos

# *******************************************************
def percorreArvore(self, percurso=percursos.PRE_ORDEM):
    if percurso == percursos.PRE_ORDEM:
      self.__preOrdem(self.__raiz)
    elif percurso == percursos.IN_ORDEM:
      self.__inOrdem(self.__raiz)
    elif percurso == percursos.POST_ORDEM:
      self.__postOrdem(self.__raiz)

def __MontaAB(self, n):
  if n == 0:
      return None

  novoNo = cNo.cNo(cArvoreBinaria.chave)
  cArvoreBinaria.chave += 1
  self.__numNos += 1

  n_restantes = n - 1
  n_esq = n_restantes // 2
  n_dir = n_restantes - n_esq

  filho_esq = self.__MontaAB(n_esq)
  novoNo.setFilhoEsq(filho_esq)

  filho_dir = self.__MontaAB(n_dir)
  novoNo.setFilhoDir(filho_dir)

  return novoNo
# *******************************************************
  def __preOrdem(self, raiz):
    if raiz is not None:
      print(raiz.getDado(), end=' ')
      self.__preOrdem(raiz.getFilhoEsq())
      self.__preOrdem(raiz.getFilhoDir())

  def __inOrdem(self, raiz):
    if raiz is not None:
      self.__inOrdem(raiz.getFilhoEsq())
      print(raiz.getDado(), end=' ')
      self.__inOrdem(raiz.getFilhoDir())

  def __postOrdem(self, raiz):
    if raiz is not None:
      self.__postOrdem(raiz.getFilhoEsq())
      self.__postOrdem(raiz.getFilhoDir())
      print(raiz.getDado(), end=' ')
  
# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':
 arvore = cArvoreBinaria(20)

print("chave =", arvore.chave)

print("\nPercurso em Pré-Ordem:")
print("======================")
arvore.percorreArvore(percursos.PRE_ORDEM)
print("\n======================")

print("Percurso em In-Ordem:")
print("======================")
arvore.percorreArvore(percursos.IN_ORDEM)
print("\n======================")

print("Percurso em Pós-Ordem:")
print("======================")
arvore.percorreArvore(percursos.POST_ORDEM)
print("\n======================")
   

