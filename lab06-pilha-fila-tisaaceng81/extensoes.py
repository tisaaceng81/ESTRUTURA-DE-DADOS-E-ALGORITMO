from pilha import pilha
from vetor import vetor
import random

# Avaliação de uma expressão pós-fixa (agora com mapeamento de variáveis para valores)
def avaliar_posfixa(expressao, valores_variaveis):
    p = pilha(100)
    for token in expressao.split():
        if token.isdigit():
            p.empilhar(int(token))
        elif token.isalpha():
            if token in valores_variaveis:
                p.empilhar(valores_variaveis[token])
            else:
                raise Exception(f"Variável '{token}' sem valor atribuído")
        else:
            b = p.desempilhar()
            a = p.desempilhar()
            if token == '+':
                p.empilhar(a + b)
            elif token == '-':
                p.empilhar(a - b)
            elif token == '*':
                p.empilhar(a * b)
            elif token == '/':
                p.empilhar(a // b)  # divisão inteira
            elif token == '^':
                p.empilhar(a ** b)
    return p.desempilhar()

# Validação de parênteses
def validar_parenteses(expressao):
    p = pilha(100)
    for char in expressao:
        if char == '(':
            p.empilhar(char)
        elif char == ')':
            if p.tamanho == 0:
                return False
            p.desempilhar()
    return p.tamanho == 0

# Geração de expressão infixa válida
def gerar_expressao_infixa_valida(tamanho=7):
    operandos = [chr(random.randint(65, 90)) for _ in range((tamanho + 1) // 2)]
    operadores = random.choices(['+', '-', '*', '/', '^'], k=len(operandos) - 1)

    expressao = []
    for i in range(len(operandos)):
        expressao.append(operandos[i])
        if i < len(operadores):
            expressao.append(operadores[i])
    
    # Adiciona parênteses aleatórios (sempre fechando)
    if len(expressao) >= 3:
        i = random.randint(0, len(expressao) - 3)
        expressao.insert(i, '(')
        expressao.insert(i + 4, ')')

    return ''.join(expressao)

# Conversão com visualização passo a passo
def infixo_para_posfixo_visual(expressao):
    operadores = pilha(100)
    posfixa = vetor(100)
    precedencia = {'+':1, '-':1, '*':2, '/':2, '^':3}

    print(f"Expressão: {expressao}")
    for char in expressao:
        print(f"\nAnalisando: {char}")
        if char.isalnum():
            posfixa.inserir(char)
        elif char == '(':
            operadores.empilhar(char)
        elif char == ')':
            while operadores.tamanho > 0 and operadores.topo() != '(':
                posfixa.inserir(operadores.desempilhar())
            operadores.desempilhar()
        else:
            while (operadores.tamanho > 0 and operadores.topo() != '(' and
                   precedencia[char] <= precedencia.get(operadores.topo(), -1)):
                posfixa.inserir(operadores.desempilhar())
            operadores.empilhar(char)

        # Impressão só dos dados válidos no vetor
        print("Saída:", ' '.join(str(posfixa.obter(i)) for i in range(posfixa.tamanho)))
        print("Pilha :", end=" ")
        operadores.imprimir_vertical()

    while operadores.tamanho > 0:
        posfixa.inserir(operadores.desempilhar())

    print("\nExpressão Pós-fixa final:", ' '.join(str(posfixa.obter(i)) for i in range(posfixa.tamanho)))
    return posfixa

# Testes automáticos
def testar_varias():
    for _ in range(5):
        expr = gerar_expressao_infixa_valida()
        print("="*40)
        print("Expressão infixa gerada:", expr)
        if not validar_parenteses(expr):
            print("Erro: parênteses inválidos")
            continue
        posfixa = infixo_para_posfixo_visual(expr)
        # Mapeia variáveis para valores aleatórios
        variaveis = set(ch for ch in expr if ch.isalpha())
        valores = {v: random.randint(1, 9) for v in variaveis}
        print("Mapeamento de variáveis:", valores)
        try:
            resultado = avaliar_posfixa(' '.join(posfixa.obter(i) for i in range(posfixa.tamanho)), valores)
            print("Avaliação pós-fixa:", resultado)
        except Exception as e:
            print("Erro na avaliação pós-fixa:", e)
        print("-" * 20)

if __name__ == "__main__":
    testar_varias()
