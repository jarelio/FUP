N = int(input("Digite o valor de N: "))
S = 0
for i in range(1,N+1):
    S = S + (1/(i**i))
print("S =",S)
