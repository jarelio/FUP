potencia_numero = 1
numero1 = float(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
for i in range(0,numero2):
    potencia_numero = numero1 * potencia_numero
print ("A potência dos números %.2f e %d é = %.3f" %(numero1,numero2,potencia_numero))
