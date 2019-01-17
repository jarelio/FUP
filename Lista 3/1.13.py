numeros_pares = 0
numeros_impares = 0
continua = True
print("Digite 0 para pausar a execução")
while continua:
    numero = int(input("Número: "))
    if (numero == 0):
        continua = False
    elif (numero%2 == 0):
        numeros_pares +=1
    elif (numero%2 != 0):
        numeros_impares +=1
print("A quantidade de números pares é:",numeros_pares)
print("A quantidade de números impares é:",numeros_impares)        
