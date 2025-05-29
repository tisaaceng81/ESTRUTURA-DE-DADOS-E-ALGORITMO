[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/0k3F5Fje)
# Lab05 - Listas Encadeadas

## Objetivos:

1. Reforçar o conceito de encadeamento e sua relação com alocação dinâmica de memória;
2. Reiterar o papel dos **TADs/Classes** *Nó* e *Lista Encadeada*;
3. Implementar as operações básicas de uma **Lista Simplesmente Encadeada** e suas variantes;
4. Aprofundar o entendimento do **TAD** *Lista Encadeada* implementando operações mais complexas;
5. Analisar a complexidade de cada uma das operações implementadas.

## Exercícios:

Leia atentamente a seção 10.2 de [1]. Garanta que compreendeu os conceitos apresentados e em caso de dúvida consulte o professor ou os monitores pelo *Discord*. 

Em seguida, analise com cuidado os módulos *cNo.py* e *cLSE.py* em termos da sua estrurura. Em caso de dúvidas, consulte novamente o professor ou os monitores pelo *Discord*.

Agora, faça o que se pede:

1. Implemente as operações básicas de: 
	1. Impressão da lista;
	2. Inserção de novos elementos;
		1. No inicio da lista;
		2. No final da lista;
		3. Mantendo a lista ordenada.
	3. Busca por um elemento da lista;
	4. Remoção de um elemento da lista.
2. Teste as operações implementadas no seu módulo;
3. Atualize o programa *mainListaEncadeada.py*, para efetuar testes de uso do seu TAD.
4. Analise a complexidade de cada uma das operações implementadas na sua estrutura de dados. 

## Exercícios Selecionados:

1. Utilizando o **TAD** *LSE* faça com que ele tenha suporte para listas ordenadas e não ordenadas. A definição da ordenação deve ser feita no construtor da classe (por *default* a lista deve ser não ordenada). A partir dai todas as operações acionadas deve manter ou não a condição de ordenação. 
2. Crie um novo TAD *Lista Duplamente Encadeada - LDE*, onde cada nó agora armazena além de seu sucessor seu predecessor. Promova as modificações necessárias em todas as operações. 
3. Crie um novo **TAD** *Lista Encadeada Circular - TEC* onde o último elemento da lista sempre aponta para o primeiro, formando um ciclo fechado.  Promova as modificações necessárias em todas as operações.
4. Para cada variante de **lista Encadeada** analise a complexidade de cada uma de suas operações. 

# Referências:

[1] 	Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. Algoritmos – Teoria e Prática. Editora Campus. 3a Edição, 2012..

[2] 	Canning, J., Broder, A., Lafore, R. **Data Structures & Algorithms in Python**. Addison-Wesley. 2022. 
