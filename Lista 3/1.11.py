somatorio = 0
limite_inferior = int(input("Digite o limite inferior: "))
limite_superior = int(input("Digite o limite superior: "))
print("Números pares entre os limites: ")
for numero in range(limite_inferior+1,limite_superior):
    if (numero%2==0):
        print(numero,"",end='')
    somatorio = numero+somatorio
print("\nO somatório dos números entre os limites é:",somatorio)
