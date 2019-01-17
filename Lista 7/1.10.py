'''Faça um programa para validar uma senha digitada pelo usuário. A senha deve ter
pelo menos uma letra maiúscula, pelo menos uma letra minúscula, pelo menos um
dígito, deve ter no mínimo 8 e no máximo 15 caracteres.'''

maiu = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
minu = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
digito2 = ["0","1","2","3","4","5","6","7","8","9"]

print("A senha deve conter: \n* 8 - 15 caracteres \n* 1 letra maiúscula \n* 1 letra minúscula \n* 1 Dígito")
senha = input("\nDigite a senha: ")

qnt_carac = False
digito = False
minuscula = False
maiuscula =  False

#Verifica tamanho da senha
if (len(senha) >= 8 and len(senha) <= 15):
    qnt_carac = True
    
#Verifica Digito, Maiuscula e Minuscula
for i in range(0,len(maiu)):
    if maiu[i] in senha:
        maiuscula = True
    if minu[i] in senha:
        minuscula = True
for i in range(0,len(digito2)):
    if digito2[i] in senha:
        digito = True
            
if qnt_carac and digito and minuscula and maiuscula:
    print("Senha Válida")
else:
    print("Senha inválida")
