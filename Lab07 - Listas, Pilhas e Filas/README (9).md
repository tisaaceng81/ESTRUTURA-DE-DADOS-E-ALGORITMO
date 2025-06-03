[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WiRE4q-V)
# Lab07 - Listas, Pilhas e Filas

## Objetivos:

1. Reforçar os conceitos das estruturas de dados *Lista Encadeada*, *Pilha* e *Fila*;
2. Aprofundar a compreensão das estruturas de dados, aplicando-as na resolução de problemas. 

## Exercícios: 

1. A partir do TAD *Lista Simplesmente Encadeada* construido durante as aulas, estenda as suas operações básicas acrescentando os seguinte métodos:

    a. **Busca de todas as ocorrencias de uma chave**: retorna a quantidade de ocorrencias de uma chave **k** dentro da lista.

    b. **Remover todas as ocorrencias de uma chave**: remove todas as ocorrencias de uma chave **k** da lista.  

    c. **Junção de Listas**: a lista recebe como parametro uma segunda lista **l** que deve ser adicionada ao final da original (*self*). Ao final da operação a lista **l** fica vazia. 

    d. **Mesclagem de listas**: a lista recebe como parametro uma lista **l** e é feita uma mesclagem (*merge*) dos elementos da lista original (*self*) com os elementos de **l**. Caso a lista seja ordenada, a mesclagem deve ser feita mantendo a ordenação, no caso contrário a mesclagem deve ser feita um a um com os elementos de cada lista. 

    A mesclagem dos elementos da lista **l** traz os elementos para a lista original (*self*), portanto a segunda lista deve terminar vazia ao final da operação. 

    e. **Comparação de Listas**: recebe como parametro uma segunda lista **l** e retorna *true* se **l** e a lista original (*self*) possuem os mesmos elementos, e *false* caso contrário. 

2. Dada uma *string* contendo uma palavra, implemente um algoritmo baseado em um (ou mais) dos TADs desse Lab
que determine se a palavra é ou não um palíndromo. Justifique a sua escolha em função da carateristica do problema. 

3. Utilizando as estruturas de dados **Pilha** e/ou **Fila**, faça o que se pede:

    a. Mostre como é possível implementar uma **fila** eficientemente utilizando duas **pilhas**. Analise a complexidade do seu algoritmo.

    b. Mostre como é possível implementar uma **pilha** eficientemente utilizando duas **filas**. Analise a complexidade do seu algoritmo. 

    c. Dada uma *string* com caracteres, remova recursivamente todos os caracteres adjacentes duplicados da *string*. A saída não pode conter nenhum caracter duplicado adjacente. Exemplos: careermonk -> camonk; mississippi -> m. 

    d. **Maior valor em uma janela deslizante**: Dado um vetor A[] com uma janela deslizante de tamanho k, que se move ao longo do vetor uma posição por vez da esquerda para a direita. Assuma que apenas os valores dentro da janela são visiveis. Determine o valor da maior soma dos elementos dentro da janela, ao longo de sua passagem pelo vetor. 

    Por exemplo, para o vetor A = [1 3 -1 -3 5 3 6 7] e uma janela de dimensão k = 3, o valor da maior soma será 7. 

    Analise a complexidade do seu algoritmo. Pense em uma solução "ótima" para o problema. 

    e. Implemente o TAD **Fila** utilizando um vetor circular com **n** posições livres. Codifique o módulo e um programa principal que promova o teste das operações da **Fila**. Não esqueça de testar as situações críticas da **Fila**. 

# Referências:

[1] Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. Algoritmos – Teoria e Prática. Editora Campus. 3a Edição, 2012.

[2] Canning, J., Broder, A., Lafore, R. **Data Structures & Algorithms in Python**. Addison-Wesley. 2022. 

[3] Goodrich,M.T., Tamassia,R., Goldwasser,M.H., **Data Structures and Algorithms in Python**. Wiley. 2013.
