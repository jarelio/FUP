#1.12. Encontre o maior elemento de um array de inteiros.

inteiros = [2,2,3,4,5,2,3,4,8,1,2,3,4,5]
tamanho = len(inteiros)-1
maior_inteiro = inteiros[tamanho]

def maiorint(inteiros,tamanho,maior_inteiro):
    if inteiros[tamanho-1] > maior_inteiro:
        maior_inteiro = inteiros[tamanho-1]
    if tamanho == 1:
        return maior_inteiro
    else:
        return maiorint(inteiros,tamanho-1,maior_inteiro)
    
print("Lista:",inteiros)    
print("Maior inteiro:",maiorint(inteiros,tamanho,maior_inteiro))
