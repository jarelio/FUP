#Gere o termo de ordem n da série de Fibonacci.
numero = int(input("Digite o número da ordem de Fibonacci: "))
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
sequencia = ""
for x in range(1,numero+1):
    sequencia = sequencia + str(fibonacci(x)) + " "
print("Ordem de Fibonacci até o %dº termo: %s" %(numero,sequencia))
