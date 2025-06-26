# Exercício Pontuado: Árvore Binária de Busca (ABB)

> **Autor:** Tiago Isaac dos Santos Carneiro
> 
> **Disciplina:** Estrutura de Dados e Algotitmos
> 
> **Objetivo:** Implementação completa de uma Árvore Binária de Busca  com operações de inserção, remoção, busca, espelhamento, contagens e visualização hierárquica.

---

##  Estrutura do Exercício
 arvore-binaria
 
├── cNo.py # Classe do nó da árvore

├── cABB.py # Classe principal da árvore binária de busca

├── main.py # Interface de interação com o usuário (CLI)

├── dados.txt # Arquivo persistente de dados (valores da árvore)

└── README.md # Relatório e explicação do projeto

---

##  Funcionalidades

- Inserção e remoção de nós
- Busca por valor
- Contagem de tipos de nós:
  - Folhas
  - Nós completos
  - Nós semi-cheios
- Altura da árvore
- Comparações entre duas árvores (estrutura e identidade)
- Espelhamento da árvore (in-place ou cópia)
- Impressão visual da árvore em formato hierárquico
- Listagem e remoção de nós por intervalo
- Modo interativo (`menu`) e modo por linha de comando (`sys.argv`)

---

##  Complexidade dos Métodos

| Método                     | Complexidade (média/pior) | Descrição |
|---------------------------|---------------------------|-----------|
| `inserir(dado)`           | `O(log n) / O(n)`          | Insere valor mantendo ordem |
| `buscar(dado)`            | `O(log n) / O(n)`          | Busca valor na árvore |
| `remover(dado)`           | `O(log n) / O(n)`          | Remove valor, trata 3 casos |
| `altura()`                | `O(n)`                     | Calcula altura da árvore |
| `contarNos(tipo)`         | `O(n)`                     | Conta nós por tipo |
| `contarNosTotal()`        | `O(n)`                     | Total de nós |
| `percorreArvore()`        | `O(n)`                     | Pré, In, Pós, Nível |
| `espelhar()`              | `O(n)`                     | Inverte esquerda/direita |
| `gerarEspelhada()`        | `O(n)`                     | Gera cópia espelhada |
| `estruturalmenteIgual()`  | `O(n)`                     | Compara forma estrutural |
| `identica()`              | `O(n)`                     | Compara forma e valores |
| `imprimirArvore()`        | `O(n)`                     | Imprime em árvore hierárquica |
| `listarIntervalo()`       | `O(n)`                     | Lista nós em faixa [min, max] |
| `removerIntervalo()`      | `O(n log n)`               | Remove nós da faixa |

---
##  Execução

### Modo Interativo (menu)
```bash
- python main.py
```


### Modo por Linha de Comando
```bash
- python main.py inserir 10 5 15
- python main.py imprimir
- python main.py remover 5
- python main.py estruturalmente_iguais 10 5 15 -- 10 4 16
```

## Testes Realizados
```bash
- Testes de inserção duplicada
- Testes de remoção com:
   Nenhum filho
   Um filho
   Dois filhos
- Espelhamento e reespelhamento
- Árvores com diferentes formas e valores para comparações
```
   
 Referências Bibliográficas:

- Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. **Algoritmos – Teoria e Prática**. Editora Campus. 3a Edição, 2012.

- Canning, J., Broder, A., Lafore, R. **Data Structures & Algorithms in Python**. Addison-Wesley. 2022.
- **Markdown Cheat Sheet**. https://www.markdownguide.org/cheat-sheet/



