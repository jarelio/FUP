'''A série de Fibonacci é formada pela seqüência:
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
Escreva um programa que armazene em um vetor os 50 primeiros termos da série de
FIBONACCI. Após isso, o programa deve imprimir todos os valores armazenados.'''
lista = [1,1]
for contador in range(1,49):
    lista.append(lista[contador]+lista[contador-1])
for numeros in lista:
    print(numeros,end=" ")
