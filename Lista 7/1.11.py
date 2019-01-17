'''1.11. Implemente um programa que leia uma data (cadeia de caracteres) no formato
dd/dd/dddd e indica se o texto lido é uma data válida ou não. São aceitas datas tanto no
formato brasileiro quanto no formato americano. Se a data lida for válida, indicar se ela
está no formato brasileiro ou no formato americano.'''

#Americano: MM/DD/AAAA
#Brasileiro: DD/MM/AAAA

data = input("Digite a data no seguinte formato (dd/dd/dddd): ")
data = data.split("/")
if int(data[0]) > 30 or int(data[1]) > 30 or int(data[2])< 1 or int(data[0]) == 0 or int(data[1]) == 0:
    print("Data inválida")
else:
    print("Data válida")
    if int(data[0]) > 12 and int(data[1]) < 13:
        print("Data no formato brasileiro (DD/MM/AAAA)")
    elif int(data[1]) > 12 and int(data[0]) < 31:
        print("Data no formato americano (MM/DD/AAAA)")
    else:
        print("Não foi possivel determinar o formato")
