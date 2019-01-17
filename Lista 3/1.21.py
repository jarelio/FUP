numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
contador = 1
while contador<=numero1 and contador<=numero2:
    if(numero1%contador == 0 and numero2%contador == 0):
        mdc = contador
    contador+=1
print("O maior divisor comum entre %d e %d é = %d" %(numero1,numero2,mdc))
