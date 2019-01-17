numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
resto = numero1
quociente = 0
while (resto>=numero2):
    resto = resto - numero2
    quociente +=1
print("O quociente da divisão é igual a:",quociente)
