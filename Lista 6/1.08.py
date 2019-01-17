#Gere o termo de ordem n da série de Fibonacci.

def fibonacci(num):
    if num < 2:
        return num
    else:
      return fibonacci(num-1) + fibonacci(num-2)

num = int(input("Digite o número de ordem da série: "))
print(fibonacci(num))
