[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MP6zaIns)
# Lab09 - Árvore Binária

## Objetivos:

1. Reforçar o conceito da estrutura de dados *Árvore*;
2. Codificar o TAD/Classe *ArvoreBinaria* utilizando a linguagem *Python*;
3. Aprofundar a compreensão dessa estrutura de dados. 

## Exercicios: 

Com base na implementação parcial do **TAD Árvore Binária**, faça o que se pede.

1. Analise os módulos *cNo.py* e *cArvoreBinaria.py*. Neles apenas os métodos básicos e um código de teste da classe são fornecidos. Repare que:

    * Alguns métodos das classes possuem **__** no inicio de seu identificador. O que isso significa?
    * O atributo **chave** está definido fora do construtor da classe. Qual a diferença para os atributos definidos dentro do construtor?

2. Implemente o método **__MontaAB** que recebe como parametro quantos nós a árvore binária irá conter. O algoritmo desse método deve seguir os seguintes passos:

    * Aloca um nó para a raiz da sub-árvore atual;
    * Calcula quantos nós restam para inclusão;
    * Divide a quantidade de nós restantes para as sub-árvores direita e esquerda;
    * *Monta* a sub-árvore esquerda;
    * *Monta* a sub-árvore direita. 

3. Codifique os 3 métodos de percurso de uma árvore binária:

    * Pré-Ordem;
    * In-Ordem;
    * Pós-Ordem.

4. Modifique a classe *cNo* para que seja armazenado em cada nó o seu nível. Alterações nos métodos da classe *cArvoreBinaria* devem ser feitos para gerar e manter essa informação. 

5. Implemente um método que calcule a altura da *árvore binária*.

6. Codifique um método que calcule o número de nós da árvore, do tipo:

    * Folha (sem filhos);
    * Completo (com 2 filhos);
    * Semi-Cheio ou incompleto (com um filho).

7. Faça um método que calcule o número de nós da árvore; (sem utilizar o atributo **numNos** da classe)

8. Dadas duas árvores binárias verificar se são estruturalmente identicas, ou seja, possuem a mesma organização de nós, independente dos valores armazenados em seus nós. 

9. Dadas duas árvores binárias verificar se são identicas, ou seja, possuem a mesma organização de nós e valores armazenados. 

# Referências Bibliográficas:

Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. **Algoritmos – Teoria e Prática**. Editora Campus. 3a Edição, 2012..

Canning, J., Broder, A., Lafore, R. **Data Structures & Algorithms in Python**. Addison-Wesley. 2022.

