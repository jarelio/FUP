#1.3. Soma de dois números naturais, através de incrementos sucessivos.

n1 = int(input("Digite n1: "))
n2 = int(input("Digite n2: "))

def soma(n1,n2):
    if n2 == 0:
        return n1
    else:
        return soma(n1,n2-1) + 1

print("Soma:",soma(n1,n2))
