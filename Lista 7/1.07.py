palavra = input("Digite uma palavra: ")
i = len(palavra)-1
print("Sufixos: ")
while i != 0:
    print(palavra[i::])
    i -=1
