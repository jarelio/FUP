a = int(input("Informe o primeiro lado do triângulo: "))
b = int(input("Informe o segundo lado do triângulo: "))
c = int(input("Informe o terceiro lado do triângulo: "))

if ((a>b-c and a<b+c) and (b>a-c and b<a+c) and (c>a-b and c<a+b)):
    print("Esses valores podem ser valores dos lados de um triângulo")
else:
    print("Esses valores não podem ser valores dos lados de um triângulo")

print(b - c, "<", a, "<", b + c)
print(a - c, "<", b, "<", a + c)
print(a - b, "<", c, "<", a + b)