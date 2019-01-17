soma = 0
contador = int(input("Digite a quantidade de números: "))

for i in range(0,contador):
	numero = int(input("Digite um número: "))
	soma = soma + numero	
	i +=1
print (soma/contador)