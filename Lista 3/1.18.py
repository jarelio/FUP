continua = True
contador = 2
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

while (continua and contador<=numero1 and contador<=numero2):
    if (numero1%contador == 0 and numero2%contador == 0):
        continua = False
    contador +=contador
if (continua):
       print("Os dois números são primos entre si")
else:
       print("Os dois números não são primos entre si")
        
