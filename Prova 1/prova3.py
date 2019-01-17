numero = int(input("Digite um número: "))
i = 1
cont = 0
continua = True
while numero >= 0 and continua:
    numero = numero - i
    i +=2
    if numero <= 0:
        continua = False
    cont +=1
    print(numero)
if numero == 0:
    print("Raiz exata: ",cont)
else:
    print("Raiz aproximada: ",cont-1)
