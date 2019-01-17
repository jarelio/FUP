a = int(input("Informe o primeiro lado do triângulo: "))
b = int(input("Informe o segundo lado do triângulo: "))
c = int(input("Informe o terceiro lado do triângulo: "))

if ((a>abs(b-c) and a<b+c) and (b>abs(a-c) and b<a+c) and (c>abs(a-b) and c<a+b)):
    print("Esses valores podem ser valores dos lados de um triângulo pois a sentença abaixo é verdadeira:")
    if (a!=b and b!=c and a!=c):
        print ("Este é um triângulo escaleno por possuir 3 lados diferentes")
    elif (a == b and b == c):
        print("Este é um triãngulo equilátero por possuir 3 lados iguais")
    elif(a==b or a==c or b==c):
        print ("Este é um triângulo isósceles por possuir 2 lados iguais")
else:
    print("Esses valores não podem ser valores dos lados de um triângulo pois a sentença abaixo é falsa:")

print(abs(b - c), "<", a, "<", b + c)
print(abs(a - c), "<", b, "<", a + c)
print(abs(a - b), "<", c, "<", a + b)