produto_numeros = 0
numero1 = float(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
for i in range(0,numero2):
    produto_numeros = numero1 + produto_numeros
print ("O produto dos números %.2f e %d é = %.2f" %(numero1,numero2,produto_numeros))
