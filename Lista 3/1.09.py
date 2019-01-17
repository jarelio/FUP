soma_notas = 0
numero_alunos = int(input("Digite o número de alunos: "))
contador = 0
nota_maior = 0
segunda_nota_maior = 0
for i in range(1,numero_alunos+1):
    #Recebe as notas dos alunos
    print("Digite a nota do aluno",i,": ",end='')
    nota_aluno = float(input())
    #Calcula as 2 maiores notas
    if (nota_aluno > nota_maior and nota_aluno > segunda_nota_maior):
        segunda_nota_maior = nota_maior
        nota_maior = nota_aluno
    elif(nota_aluno > segunda_nota_maior):
        segunda_nota_maior = nota_aluno
    #Soma todas as notas e conta a quantidade de notas
    contador +=1
    soma_notas = nota_aluno + soma_notas
print ("A média das notas é:",soma_notas/contador)                    
print ("A nota maior é:",nota_maior)
print ("A segunda nota maior é:",segunda_nota_maior)
