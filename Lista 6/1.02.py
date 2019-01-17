num1,num2 = input("Digite os dois números: ").split(" ")
num1 = int(num1)
num2 = int(num2)
mult = 0
def multiplica(num1,num2):
  if num2 == 0:
    return num2
  elif num2 == 1:
    return num1
  else:
    return num1 + multiplica(num1,num2-1)
print("%d * %d = %d" %(num1,num2,multiplica(num1,num2)))
