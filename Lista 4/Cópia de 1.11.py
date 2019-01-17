'''1.11. Seja:
Escrever um programa que:
a) Leia o valor de n, sendo n <= 20;
b) Leia os coeficientes ai, onde i = 0, 1, 2 , ..., n;
c) Calcule o valor de P para 10 valores lidos para x;
d) Imprima o valor de x e o valor de P correspondente.'''

lista = []
contador = 0
P = 0
n = int(input("Digite o valor de n, (n<=20): "))
expoente = n
if n >20:
	print("Valor de n digitado incorreto!")
else:
	while(n!=0):
		a = float(input("Digite o valor de a: "))
		lista.append(a)
		n -=1
if (len(lista) < 10):
	print("Essa lista tem menos que 10 valores para calcular o valor de P: ")
else:
	for i in range(0,10):
		x = float(input("Digite o valor de x: "))
		P = P + lista[i]*(x**expoente)
		print("X: %.2f P: %.2f" %(x,P))
		expoente -=1