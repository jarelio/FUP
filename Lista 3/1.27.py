N = int(input("Digite o número N: "))
H = 0
for i in range(1,N+1):
    H = float(H+(1/i))
print("O valor de H é:",H)
