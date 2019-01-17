'''Escreva um programa que armazene em um vetor todos os números inteiros de 200
a 100 (em ordem decrescente). Após isso, o programa deve imprimir todos os valores
armazenados.'''

lista = []
for numero in range(200,99,-1):
    lista.append(numero)
for numeros in lista:
    print(numeros,end=" ")
