lbinario = []   
num = int(input("Digite um numero: "))
def binario(n):   
  if n > 0: 
        lbinario.append(n%2)
        n = int(n/2)
        binario(n)
binario(num)
lbinario.reverse()
print("Binário: ",end = '')
for numero in lbinario:
        print(numero,end=' ')
