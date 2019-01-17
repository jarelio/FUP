N = int(input("Digite a quantidade de termos: "))
for i in range(1,N+1):
    if (i % 3 == 1):
        print(int(i/3) + 1,end=' ')
    elif(i % 3 == 2):
        print(int(i/3) + 4,end=' ')
    else:
        print(int(i/3) + 3,end=' ')
