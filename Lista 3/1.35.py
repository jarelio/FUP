X = float(input("Digite um valor: "))
ex = 0
for i in range(1,16):
    z = 1
    i_fatorial = 1
    while z<=i:
        i_fatorial = i_fatorial * z
        z = z+1
    if (i == 1):
        ex = ex + 1 + X
    else:
        ex = ex + ((X**i)/(i_fatorial))
print("O valor do e^x é:",ex)
