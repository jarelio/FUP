from random import randint
numeros = []
sorteados = []
acertos = 0
continua = True
i = 0
while continua and i < 6:
    numero = int(input("Digite um número entre 1 e 99: "))
    if numero < 1 or numero > 99:
        continua = False
        print("Número incorreto digitado")
    else:
        numeros.append(numero)
        numero_sorteado = randint(1,100)
        sorteados.append(numero_sorteado)
    i +=1
if len(numeros) == 6 and len(sorteados) == 6:
    print("Os números sorteados foram: ",end='')
    for z in range(0,6):
        for u in range(0,6):
            if (numeros[z] == sorteados[u]):
                acertos +=1
        print(sorteados[z],end=' ')
    print("\nVocê acertou %d número(s)" %acertos)
    if (acertos == 3):
        print("Terno")
    elif(acertos == 4):
        print("Quadra")
    elif(acertos == 5):
        print("Quina")
    elif(acertos == 6):
        print("Sena")
    else:
        print("Azar")
