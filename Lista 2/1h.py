idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o seu peso: "))

if (idade<20):
    if (peso<=60):
        grupo_de_risco = 9
    elif (peso>60 and peso<=90):
        grupo_de_risco = 8
    else:
        grupo_de_risco = 7
elif (idade>=20 and idade <=50):
    if (peso<=60):
        grupo_de_risco = 6
    elif (peso>60 and peso<=90):
        grupo_de_risco = 5
    else:
        grupo_de_risco = 4
else:
    if (peso<=60):
        grupo_de_risco = 3
    elif (peso>60 and peso<=90):
        grupo_de_risco = 2
    else:
        grupo_de_risco = 1

print ("Você tem peso igual a",peso,"e se encaixa no grupo de risco: ",grupo_de_risco)