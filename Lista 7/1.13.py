'''1.13. Implemente um programa que gere aleatoriamente um
CAPTCHA de seis caracteres, o qual obrigatoriamente deve conter: letras maiúsculas,
letras minúscula e dígitos. O programa deve exibir o CAPTCHA gerado e solicitar que
o usuário digite o valor exibido. Em seguida, o programa deve ler o texto digitado pelo
usuário e verificar se este corresponde ao CAPTCHA gerado. Observe que, durante esta
comparação, não se faz diferença entre letras maiúsculas ou minúsculas. O programa
deve imprimir uma mensagem dizendo se o usuário passou ou não do teste.'''
import random
opco = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N",
        "O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b",
        "c","d","e","f","g","h","i","j","k","l","m","n","o","p",
        "q","r","s","t","u","v","w","x","y","z","0","1","2","3",
        "4","5","6","7","8","9"]
captcha = ""
cont = 0

#Criação do CAPTCHA
for i in range(0,6):
    aleatorio = random.randint(0,len(opco))
    captcha = captcha + opco[aleatorio]
    
#Recebimento da Resposta
resposta = input("Digite o seguinte CAPTCHA -->%s<-- \nResposta: " %captcha)

#Verificaçao de Cada Dígito
for i in resposta:
    if i.lower() in captcha:
        cont +=1
    elif i.upper() in captcha:
        cont +=1

#Resultado
if cont == 6:
    print("\nCAPTCHA correta! \n\nResposta: %s \nCAPTCHA: %s" %(resposta,captcha)) 
else:
    print("\nCAPTCHA incorreta! \n\nResposta: %s \nCAPTCHA: %s" %(resposta,captcha)) 
