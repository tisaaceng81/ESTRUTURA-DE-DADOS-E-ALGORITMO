# Lab09 - Árvore Binária 

import cNo
import cArvoreBinaria

import sys

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

  n = 20
  if (len(sys.argv) > 1):
      n = int(sys.argv[1])
      if n < 0:
          n = 20

  arvore = cArvoreBinaria.cArvoreBinaria(n)

  print("Percurso em Pré-Ordem:")
  print("======================")
  arvore.percorreArvore(cArvoreBinaria.percursos.PRE_ORDEM)
  print("======================")

  print("Percurso em In-Ordem:")
  print("======================")
  arvore.percorreArvore(cArvoreBinaria.percursos.IN_ORDEM)
  print("======================")

  print("Percurso em Post-Ordem:")
  print("======================")
  arvore.percorreArvore(cArvoreBinaria.percursos.POST_ORDEM)
  print("======================")
