numero = int(input("Digite um número: "))
contador = 1
print("Os divisores de %d são: " %numero)
while (contador<=numero):
    if (numero%contador==0):
        divisor = contador
        print (divisor,end=' ')
    contador +=1    
