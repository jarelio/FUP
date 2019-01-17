contador_par = 0
contador_impar = 0
maior_par = 0
menor_impar = 0
soma_par = 0
soma_impar = 0
print("Digite números, caso ele seja negativo o programa irá parar: ",end='')
numero = int(input())
menor_impar = numero
maior_par = numero
while numero>=0:
	numero = int(input())
	if(numero<0):
		break
	if (numero % 2 == 0):
		soma_par = soma_par + numero
		contador_par+=1
		if (numero > maior_par):
			maior_par = numero
	else:
		soma_impar = soma_impar + numero
		contador_impar+=1
		if(numero < menor_impar):
			menor_impar = numero
print("A média dos números pares é: ",soma_par/contador_par)
print("A média dos números impares é: ",soma_impar/contador_impar)
print("O maior número par é: ",maior_par)
print("O menor número ímpar é: ",menor_impar)