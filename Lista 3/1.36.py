N = int(input("Digite o valor de N: "))
z = 0.0
troca = 1
S = 0.0
while N>=0:
	#Calculo do N_fatorial
	N_fatorial = 1.0
	i = 1.0
	while i<=N:
		N_fatorial = N_fatorial * i
		i+=1
	N = N - 1

	#Calculo do i_fatorial
	i_fatorial = 1.0
	x = 1.0 
	while x<=z:
		i_fatorial = i_fatorial * x
		x+=1
	z = z+2.0

	if (troca == 1):
		S = S + (N_fatorial / i_fatorial)
		troca = 0
	else:
		S = S - (N_fatorial / i_fatorial)
		troca = 1
print(S)