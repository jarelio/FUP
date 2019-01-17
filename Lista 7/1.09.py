email = input("Digite o e-mail: ")
valor = "E-mail Inválido"
for i in range(0,len(email)):
    if email[i] == "@":
        if email[0:i] != "" and email[i+1::] != "":
            if "." in (email[i+1::]) and "." not in (email[i+1]): 
                valor = "E-mail Válido"
print(valor)
