x = float(input("Digite o valor de x: "))

if (x<=1):
    fx = 1
elif(x>1 and x<=2):
    fx = 2
elif(x>2 and x<=3):
    fx = x**2
elif(x>3):
    fx = x**3
print ("O valor de f(x) é: ",fx)