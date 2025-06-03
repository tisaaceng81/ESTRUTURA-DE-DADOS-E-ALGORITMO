class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

if __name__ == "__main__":
    print("Teste do módulo No")
    no1 = No(5)
    no2 = No(10)
    
    print("Dado:", no1.dado)
    print("Próximo:", no2.proximo)
