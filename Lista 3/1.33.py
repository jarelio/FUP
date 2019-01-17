X = float(input("Digite um valor: "))
Xrad = X * 0.01745329252
S = 0
troca = 1
for i in range(1,16):
    if (i%2 != 0):
        z = 1
        i_fatorial = 1
        while z<=i:
            i_fatorial = i_fatorial * z
            z = z+1
        if (troca == 1):
            S = S + ((Xrad**i)/(i_fatorial))
            troca = 0
        else:
            S = S - ((Xrad**i)/(i_fatorial))
            troca = 1
print("O valor do seno de %.2f é %.2f" %(X,S))
