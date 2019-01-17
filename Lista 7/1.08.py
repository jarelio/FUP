'''Implemente um programa que leia uma cadeia de caracteres e um número inteiro
positivo “n”. O programa deve imprimir todas as sub-cadeias da cadeia original de
comprimento igual a “n”.'''

cadeia = input("Digite a cadeia: ")
n = int(input("Digite o numero: "))
cadeia = list(cadeia)

print("Sub-cadeias de %d comprimento:" %n,end=" ")

if (n > len(cadeia)):
    print("Excedeu o comprimento da palavra!")

for i in range(0,(len(cadeia)-n)+1):
    print(end=' ')
    for j in range(i,n+i):
        print(cadeia[j],end='')
