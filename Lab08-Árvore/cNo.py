# ##################################################
# Classe cNo de uma Árvore Binária
# ##################################################

class cNo:

  def __init__(self, dado=0, nivel=0):
    self.__dado    = dado
    self.__fEsq    = None
    self.__fDir    = None
    self.__nivel   = nivel

  def getDado(self):
    return self.__dado
  
  def setDado(self, valor):
    self.__dado = valor
  
  def getFilhoEsq(self):
    return self.__fEsq
  
  def setFilhoEsq(self, filhoEsq):
    self.__fEsq = filhoEsq
  
  def getFilhoDir(self):
    return self.__fDir
  
  def setFilhoDir(self, filhoDir):
    self.__fDir = filhoDir

  def getNivel(self):
    return self.__nivel

  def setNivel(self, nivel):
    self.__nivel = nivel

  def __str__(self):
    outStr =  f'+================================================+\n'
    outStr += f'|                  {id(self):16x}                  |\n'
    outStr += f'+================+++========+++==================+\n'
    outStr += f'| {id(self.__fEsq):16x} | {self.__dado:8} | {id(self.__fDir):16x} |\n'
    outStr += f'+================+++========+++==================+\n'
    return outStr