# ##################################################
# Classe cNo de uma Árvore Binária de Busca 
# ##################################################

class cNo:

  # *******************************************************
  def __init__(self, dado=0):
    self.__dado = dado
    self.__filhoDir = None
    self.__filhoEsc = None

  # *******************************************************
  def getDado(self):
    return self.__dado

  # *******************************************************
  def setDado(self, valor):
    self.__dado = valor

  # *******************************************************
  def __str__(self):
    outStr  = '+================================================+\n'
    outStr += f'|             {id(self):16x}                   |\n'
    outStr += '+================+++========+++==================+\n'
    outStr += f'| {id(self.__filhoEsc):16x} | {self.__dado:8} | {id(self.__filhoDir):16x} |\n'
    outStr += '+================+++========+++==================+\n'
    return outStr


# *******************************************************
# *** Teste básico ***
# *******************************************************
if __name__ == '__main__':
  print("Teste da classe cNo")
  no = cNo(42)
  print(no)
