# Jogo UNO

Este Trabalho implementa uma simulação do jogo UNO em Python, usando estruturas de dados personalizadas e testes manuais. O objetivo é demonstrar manipulação de coleções sem usar métodos nativos de lista (`append`, `pop`, `extend`), utilizando uma classe `Vetor` com capacidade fixa.

## Estrutura de Módulos

O jogo está organizado em três módulos principais:

### 1. `cartas.py`

* **Classe `Carta`**: representa uma carta do jogo, com atributos `cor` e `valor` e método `combina_com` para verificar jogadas válidas.
* **Classe `Vetor`**: vetor de capacidade fixa com métodos:

  * `inserir(item)`: insere um elemento no final do vetor.
  * `remover()`: remove o último elemento.
  * `__getitem__` e `__setitem__`: acesso e atribuição por índice.
  * `vazio()` e `limpar()`: verificação de vazio e limpeza do vetor.
* **Funções**:

  * `criar_baralho()`: monta o baralho completo do UNO (120 cartas).
  * `embaralhar(vetor)`: aplica o algoritmo de Fisher–Yates para embaralhar.
* **Teste manual**: bloco `if __name__ == "__main__"` que retira 7 cartas iniciais e exibe a mão.

### 2. `jogador.py`

* **Classe `Jogador`**:

  * `comprar_carta(carta)`: recebe uma carta e insere na mão.
  * `comprar_carta_com_baralho`: alias de `comprar_carta`, para compatibilidade.
  * `remover_carta(carta)`: remove uma carta da mão deslocando elementos.
  * Métodos de interação: `mostrar_mao()`, `get_carta(idx)`, `tem_carta_valida(carta_mesa)`, `escolher_carta(carta_mesa)`, `mao_vazia()`.
* **Teste manual**: bloco `if __name__ == "__main__"` que compra 7 cartas e mostra a mão.

### 3. `simulador2.py`

* **Entrada**: parâmetro de linha de comando `num_jogadores` (5–10, padrão 7).
* **Fluxo**:

  1. Criação e embaralhamento do baralho.
  2. Criação de `Vetor` de jogadores e distribuição de 7 cartas.
  3. Inicialização da pilha de descarte com uma carta.
  4. Loop de jogo, alternando turnos, exibindo estado do deck, descarte e mãos.
  5. Jogada de cartas, compra quando necessário e aplicação de efeitos (`Pular`, `Reverter`, `+2`, `+4`).
  6. Verificação de vitória.

## Como Executar

```bash

# Executar com 7 jogadores (padrão)
python simulador2.py

# Executar com número específico de jogadores (5 a 10)
python simulador2.py 6
```

## Complexidade do Programa

* **Embaralhar (Fisher–Yates)**: O(n), onde n ≈ 120.
* **Operações em `Vetor`**:

  * `inserir` e `remover` do fim: O(1).
  * `remover_carta` (deslocamento): O(m), onde m é tamanho da mão.
* **Turno de jogo**: O(p × t × m), com p jogadores, t turnos e m cartas na mão.

## Regras Implementadas


---

##  Algoritmo e Estrutura

###  Regras Implementadas

- Combinação de cartas por **cor** ou **valor**
- Suporte a cartas especiais:
  - `Pular` (skip)
  - `Reverter` (reverse)
  - `+2` e `+4`
  - `Coringa` (escolha de cor)
- Compra de carta se não houver jogada válida
- Reversão de sentido do jogo
- Detecção automática de vitória (mão vazia)

## Conclusão

Este projeto demonstra:

* Implementação de um jogo de cartas completo sem métodos nativos de lista.
* Uso de estruturas de dados de capacidade fixa.
* Lógica de jogo UNO, incluindo efeitos de cartas especiais.
* Testes manuais integrados a cada módulo.

## Referências Bibliográficas

[1] Wikipedia. UNO. disponível em: https://pt.wikipedia.org/wiki/Uno_(jogo_de_cartas)

[2] Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. Algoritmos – Teoria e Prática. Editora Campus. 4a Edição, 2022.

[3] Canning, J., Broder, A., Lafore, R. Data Structures & Algorithms in Python. Addison-Wesley. 2022.

[4] Erica Vartanian, "6 coding best practices for beginner programmers". Disponível em: https://www.educative.io/blog/coding-best-practices

[5] Matt Cone, Markdown Cheat Sheet - A quick reference to the Markdown syntax. Disponível em: https://www.markdownguide.org/cheat-sheet/

[6] GitHub Docs. Introdução à escrita e formatação no GitHub. Disponível em: https://docs.github.com/pt/github/writing-on-github/getting-started-with-writing-and-formatting-on-github