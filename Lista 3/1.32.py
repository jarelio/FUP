S = 0
troca = 1
for i in range(1,52):
    if (i%2 != 0):
        if (troca == 1):
            S +=(1/(i**3))
            troca = 0
        else:
            S -=(1/(i**3))
            troca = 1
pi = (S*32)**(1/3)
print(pi)
