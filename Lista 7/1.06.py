palavra = input("Digite a palavra: ")
print("Prefixos: ")
for i in range(1,len(palavra)):
    print(palavra[0:i])
