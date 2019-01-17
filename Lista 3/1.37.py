contador_mulher = 0
altura_mulheres = 0
altura_maior = 0
contador_turma = 0
soma_alturas = 0
altura_menor = 0
for i in range(0,4):
	print("Digite a altura e o código do sexo (1):Masculino (2): Feminino: ",end='')
	altura = float(input())
	codigo = int(input())
	if (i == 0):
		altura_maior = altura
		altura_menor = altura
	#Maior e menor altura
	if (altura > altura_maior):
		altura_maior = altura
	elif(altura < altura_menor):
		altura_menor = altura
	#Media das mulheres
	if (codigo == 2):
		altura_mulheres = altura_mulheres + altura
		contador_mulher = contador_mulher+1
	#Media da turma	
	soma_alturas = soma_alturas + altura
	contador_turma = contador_turma + 1
print("A média de altura das mulheres é: ",altura_mulheres/contador_mulher)
print("A média de altura da turma é: ",soma_alturas/contador_turma)
print("A maior altura é: ",altura_maior)
print("A menor altura é: ",altura_menor)