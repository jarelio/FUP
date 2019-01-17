num = int(input("Digite o número (limite superior): "))
print("Os números múltiplos de 3 e 5 entre o intervalo são: ")
for multiplos in range(1,num+1):
    if (multiplos%3 == 0 and multiplos%5 == 0):
        print(multiplos,"",end='')
