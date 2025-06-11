# ##################################################
# Classe Cno de uma Árvore Binária
# ##################################################

class cNo:

# *******************************************************
# *******************************************************
  def __init__(self, dado=0):
    self.__dado   = dado
    self.__fEsq   = None
    self.__fDir   = None
  
# *******************************************************
  def getDado(self):
    return self.__dado
  
# *******************************************************
  def setDado(self, valor):
    self.__dado = valor
  
# *******************************************************
  def getFilhoEsq(self):
    return self.__fEsq
  
# *******************************************************
  def setFilhoEsq(self, filhoEsq):
    self.__fEsq = filhoEsq
  
# *******************************************************
  def getFilhoDir(self):
    return self.__fDir
  
# *******************************************************
  def setFilhoDir(self, filhoDir):
    self.__fDir = filhoDir

# *******************************************************
# *******************************************************
  def __str__(self):

    outStr =  f'+================================================+\n'
    outStr += f'|             {id(self):16x}                   |\n'
    outStr += f'+================+++========+++==================+\n'
    outStr += f'| {id(self.__fEsq):16x} | {self.__dado:8} | {id(self.__fDir):16x} |\n'
    outStr += f'+================+++========+++==================+\n'
    return outStr

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

  pai       = cNo(10);
  print(f' {pai}');
  filhoDir  = cNo(20);
  print(f' {filhoDir}');
  filhoEsq  = cNo(30);
  print(f' {filhoEsq}');
 
  pai.setFilhoDir(filhoDir);
  pai.setFilhoEsq(filhoEsq);

  print(pai);
  print(filhoDir);
  print(filhoEsq);
