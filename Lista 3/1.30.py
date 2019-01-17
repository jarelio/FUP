a = 1
S = 0
troca = 1
for i in range(1,101):
    if (i == 1):
        S = S + 1
    if (i%2 == 0):
        if (troca == 1):
            S = S - (1/(i))
            troca = 0
        else:
            S = S + (1/(i))
            troca = 1
print("S =",S)
