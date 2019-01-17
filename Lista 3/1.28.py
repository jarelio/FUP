X = float(input("Digite um número real: "))
S=0
A=0
for i in range(1,21):
    z = 1
    i_fatorial = 1
    while z<=i:
        i_fatorial = i_fatorial * z
        z = z+1
    if (i%2 == 0):
        S = S + X/i_fatorial
    else:
        S = S - X/i_fatorial
print (S)
