a = int(input("Informe o primeiro lado do triângulo: "))
b = int(input("Informe o segundo lado do triângulo: "))
c = int(input("Informe o terceiro lado do triângulo: "))

if ((a>abs(b-c) and a<b+c) and (b>abs(a-c) and b<a+c) and (c>abs(a-b) and c<a+b)):
    print("Esses valores podem ser valores dos lados de um triângulo pois a sentença abaixo é verdadeira:")
    if (a>b and a>c):
        if (a**2 == (b**2 + c**2)):
            print ("Triângulo Retângulo")
        elif (a**2 < (b**2 + c**2)):
            print ("Triângulo Acutângulo")
        elif (a**2 > (b**2 + c**2)):
            print ("Triângulo Obtusângulo")
    elif (b>a and b>c):
        if (b**2 == (a**2 + c**2)):
            print ("Triângulo Retângulo")
        elif (b**2 < (a**2 + c**2)):
            print ("Triângulo Acutângulo")
        elif (b**2 > (a**2 + c**2)):
            print ("Triângulo Obtusângulo")
    elif(c>a and c>b):
        if (c**2 == (a**2 + b**2)):
            print ("Triângulo Retângulo")
        elif (c**2 < (a**2 + b**2)):
            print ("Triângulo Acutângulo")
        elif (c**2 > (a**2 + b**2)):
            print ("Triângulo Obtusângulo")
else:
    print("Esses valores não podem ser valores dos lados de um triângulo pois a sentença abaixo é falsa: ")

print(abs(b - c), "<", a, "<", b + c)
print(abs(a - c), "<", b, "<", a + c)
print(abs(a - b), "<", c, "<", a + b)