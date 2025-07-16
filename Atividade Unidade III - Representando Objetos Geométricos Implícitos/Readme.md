# Atividade Unidade III - Representando Objetos Geométricos Implícitos
# Aluno: Tiago Isaac dos Santos Carneiro  
#        Leonardo Ribeiro

Este projeto implementa uma **árvore VDB** (Volumetric Data Structure) aplicada à representação de **curvas implícitas bidimensionais**, com visualização gráfica usando **Pyglet**.


## Estrutura do Projeto

Lab10/
├── main.py # Módulo principal com interface gráfica e controle de visualização

├── vetor.py # Implementa TAD ArrayLimitado (sem uso de listas nativas)

├── arvore_vdb.py # Implementa a estrutura de dados VDB em árvore

├── curvas.py # Define as curvas implícitas e armazena usando TAD

├── README.md # Este relatório



---

##  Objetivo

Visualizar a construção da árvore VDB (uma árvore quad-tree adaptativa) para diferentes curvas implícitas no plano, de forma **interativa** e **didática**.

---

##  Como Executar

No terminal, execute o programa principal passando o índice da curva e, opcionalmente, o modo de visualização:

python main.py [indice_curva] [modo_visualizacao]

# Exemplo: 
python main.py 3 2

# Ou execute sem argumentos para entrar em modo interativo:
python main.py

# Controles Interativos

1 - Modo Árvore completa

2 - Modo por nível (use ↑ ↓ para alterar o nível)

3 - Modo folhas na fronteira

4 - Apenas curva

# Modos de Visualização

Modo	Descrição

1	Árvore completa recursiva

2	Visualização por nível

3	Apenas folhas da fronteira

4	Apenas curva implícita desenhada

# Curvas Suportadas

Superelipse

Quártica

Lemniscata

Coração

Coelho

Gato

As curvas são definidas como funções matemáticas f(x,y)=0 e adicionadas à estrutura ArrayLimitado no módulo curvas.py.

##  Implementação Técnica

# TAD: ArrayLimitado

O módulo vetor.py define uma estrutura própria para simular listas com capacidade fixa.
Sem uso de listas, tuplas ou dicionários nativos do Python.

Principais métodos:

adicionar(indice, valor)

remover(indice)

obter(indice)

resetar()

__len__ (tamanho atual)

# Estrutura VDB - Módulo arvore_vdb.py

Implementa uma árvore adaptativa com subdivisão de quadrantes 2D. A estrutura é construída recursivamente com base em avaliação de variação na função implícita.

Principais métodos:

construir_estrutura(funcao)

dividir_no(no, funcao)

avaliar_regiao(x, y, largura, altura, funcao)

mostrar_estrutura()

Complexidade da construção da árvore:

Pior caso: O(4^n), onde n é a profundidade máxima da árvore

Melhor caso: O(1), sem subdivisões

# Visualização - Módulo main.py

Responsável pela interface gráfica com Pyglet.
Permite alternar visualizações, renderizar curvas e explorar os nós da árvore em tempo real.

# Ações incluídas:

Controle por teclado (modos de exibição)

Cores diferentes por nível de profundidade

Representação dos nós como retângulos

Curva implícita desenhada em pixels

# Tecnologias Utilizadas
 - Python 3.10+

 - Pyglet para renderização gráfica

# Instalação das dependências:
pip install pyglet

# Complexidade Computacional

Função ou Método	Complexidade

Construção da árvore (VDB)	O(4^n) (pior caso)

Visualização recursiva	O(N) onde N = nº de nós

ArrayLimitado.adicionar()	O(1)

ArrayLimitado.obter()	O(1)

✅ Avaliação Acadêmica
Critérios exigidos e atendidos:

✔️ Relatório técnico (README completo em Markdown)

✔️ Boas práticas (modularização, comentários, TADs)

✔️ Estrutura de dados (implementação VDB funcional)

✔️ Visualização da estrutura (por nível, completa, folhas, curva)

✔️ Apresentação interativa (interface clara, atalhos de teclado)

✔️ Sem listas/tuplas nativas em todos os módulos



 # Conclusão

Este projeto demonstra domínio prático sobre TADs, recursividade, árvores adaptativas e visualização gráfica. A ausência de estruturas nativas e o uso controlado de memória evidenciam atenção a restrições didáticas e técnicas.



 # Referências Bibliográficas:

[1] Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. Algoritmos – Teoria e Prática. Editora Campus. 4a. Edição, 2022.

[2] Canning, J., Broder, A., Lafore, R. Data Structures & Algorithms in Python. Addison-Wesley. 2022.

[3] Wikipedia, Implicit Surface. https://en.wikipedia.org/wiki/Implicit_surface

[4] Museth, K. (2013). VDB: High-resolution sparse volumes with dynamic topology. ACM Trans. Graph., 32, 27:1-27:22.

[5] NVIDIA GVDB Voxels. https://developer.nvidia.com/gvdb

[6] Museth, Ken, Jeff Lait, John Johanson, Jeff Budsberg, Ron Henderson, Mihai Alden, Peter Cucka, David Hill, and Andrew Pearce. OpenVDB: an open-source data structure and toolkit for high-resolution volumes. In Acm siggraph 2013 courses, pp. 1-1. 2013.

[7] OpenVDB. https://www.openvdb.org/

[8] Museth, Ken. NanoVDB: A GPU-friendly and portable VDB data structure for real-time rendering and simulation. In ACM SIGGRAPH 2021 Talks, pp. 1-2. 2021.

[9] NVIDIA NanoVDB. https://developer.nvidia.com/nanovdb

[10] Kim, Doyub, Minjae Lee, and Ken Museth. Neuralvdb: High-resolution sparse volume representation using hierarchical neural networks. ACM Transactions on Graphics 43, no. 2 (2024): 1-21.

[11] NVIDIA NeuralVDB. https://developer.nvidia.com/rendering-technologies/neuralvdb

[12] Williams, Francis, Jiahui Huang, Jonathan Swartz, Gergely Klar, Vijay Thakkar, Matthew Cong, Xuanchi Ren et al. fvdb: A deep-learning framework for sparse, large scale, and high performance spatial intelligence. ACM Transactions on Graphics (TOG) 43, no. 4 (2024): 1-15.

[13] pyglet. pyglet Documentation. https://pyglet.readthedocs.io/en/latest/

[14] Erica Vartanian, "6 coding best practices for beginner programmers". Disponível em: https://www.educative.io/blog/coding-best-practices

[15] Matt Cone, Markdown Cheat Sheet - A quick reference to the Markdown syntax. Disponível em: https://www.markdownguide.org/cheat-sheet/

[16] GitHub Docs. Introdução à escrita e formatação no GitHub. Disponível em: https://docs.github.com/pt/github/writing-on-github/getting-started-with-writing-and-formatting-on-github