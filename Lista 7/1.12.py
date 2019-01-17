'''1.12. Implemente um programa que leia um ano, no formato dddd, e imprime o ano por
extenso.'''

mil = ["Dois","Três","Quatro","Cinco","Seis","Sete","Oito","Nove"]
cem = [" Cento"," Duzentos"," Trezentos"," Quatrocentos"," Quinhentos"," Seiscentos"," Setessentos"," Oitocentos"," Novecentos"]
esp = [" e Dez"," e Onze"," e Doze"," e Treze"," e Quatorze"," e Quinze"," e Dezesseis"," e Dezessete"," e Dezoito"," e Dezenove"]
dezena = [" e Vinte"," e Trinta"," e Quarenta"," e Cinquenta"," e Sessenta"," e Setenta"," e Oitenta"," e Noventa"]
unidade = [" e Um"," e Dois"," e Três"," e Quatro"," e Cinco"," e Seis"," e Sete"," e Oito"," e Nove"]
ano = input("Digite o ano: ")
ano = list(ano)
#Primeiro Nome
if int(ano[0]) > 1:
    ano[0] = mil[int(ano[0])-2] + " Mil"
elif int(ano[0]) == 0:
    ano[0] = ""
else:
    ano[0] = "Mil "

#Segundo Nome
if int(ano[1]) != 0:
    ano[1] = cem[int(ano[1])-1]
else:
    ano[1] = ""
    
#Terceiro Nome
if int(ano[2]) == 1:
    ano[2] = esp[int(ano[3])]
    ano[3] = ""
elif int(ano[2]) > 1:
    ano[2] = dezena[int(ano[2])-2]
elif int(ano[2]) == 0:
    ano[2] = ""

#Quarto Nome
if ano[3] != "" and int(ano[3]) != 0:
    ano[3] = unidade[int(ano[3])-1]
else:
    ano[3] = ""
    
print("Por Extenso:",end=" ")
print(" ".join("".join(ano).split()))



