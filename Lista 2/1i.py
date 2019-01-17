a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = ((b**2)-(4*a*c))
if (delta>0):
    x1 = ((b * (-1)) + (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)
    x2 = ((b * (-1)) - (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)
    print ("A primeira raiz x' é: ", x1)
    print ("A segunda raiz x'' é: ", x2)
elif (delta==0):
    x1 = ((b*(-1))/(2*a))
    print ("A única raiz dessa função é: ", x1)
else:
    print ("Essa função não tem raiz pois o delta é menor que 0")
