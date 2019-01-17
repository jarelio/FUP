numero = int(input("Digite um valor >=1: "))
expoente = 1
soma = 0
if numero >=1:
    for i in range(1,numero+1):
        if expoente == 1:
            soma = soma + (1/i**expoente)
            expoente = 2
        elif expoente == 2:
            soma = soma + (1/i**expoente)
            expoente = 3
            print(soma)
        elif expoente == 3:
            soma = soma + (1/i**expoente)
            expoente = 1
else:
    print("Número digitado incorreto")
print(soma)
