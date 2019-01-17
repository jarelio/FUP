def mult(num1,c):
    if c == 0:
        return num1
    else:
        return mult(num1,c-1) + 1
n1 = int(input("Digite o valor de n1: "))
n2 = int(input("Digite o valor de n2: "))
c = ((n1*n2)-n1)
print(mult(n1,c))
