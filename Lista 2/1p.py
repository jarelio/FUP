import math

a = float(input("Informe o primeiro lado do triângulo: "))
b = float(input("Informe o segundo lado do triângulo: "))
c = float(input("Informe o terceiro lado do triângulo: "))

if ((a>b-c and a<b+c) and (b>a-c and b<a+c) and (c>a-b and c<a+b)):
    print("Esses valores podem ser valores dos lados de um triângulo")
    if (a > b and a > c):
        if (a ** 2 == (b ** 2 + c ** 2)):
            print("Triângulo Retângulo")
            tg = math.atan2(b,c)
            tg2 = math.atan2(c,b)
            print ("Um dos ângulos internos deste triângulo é: %.2fº" %math.degrees(tg))
            print("O outro ângulo deste triângulo é: %.2fº" %math.degrees(tg2))
            print("O terceiro ângulo deste triângulo é de 90º")
    elif (b > a and b > c):
        if (b ** 2 == (a ** 2 + c ** 2)):
            print("Triângulo Retângulo")
            tg = math.atan2(a, c)
            tg2 = math.atan2(c, a)
            print("Um dos ângulos internos deste triângulo é: %.2fº" % math.degrees(tg))
            print("O outro ângulo deste triângulo é: %.2fº" % math.degrees(tg2))
            print("O terceiro ângulo deste triângulo é de 90º")
    elif (c > a and c > b):
        if (c ** 2 == (a ** 2 + b ** 2)):
            print("Triângulo Retângulo")
            tg = math.atan2(b, c)
            tg2 = math.atan2(c, b)
            print("Um dos ângulos internos deste triângulo é: %.2fº" % math.degrees(tg))
            print("O outro ângulo deste triângulo é: %.2fº" % math.degrees(tg2))
            print("O terceiro ângulo deste triângulo é de 90º")
else:
    print("Esses valores não podem ser valores dos lados de um triângulo ")