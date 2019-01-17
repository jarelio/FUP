num1,num2 = input("Digite os dois números: ").split(" ")
num1 = int(num1)
num2 = int(num2)
def multiplica(num1,num2):
  if num2 <0 and num1 <0:
    num1 = num1*(-1)
    num2 = num2*(-1)
  if num2<0:
    return num1*(-1) + multiplica(num1,num2+1)
  elif num2 == 0:
    return num2
  elif num2 == 1:
    return num1
  else:
    return num1 + multiplica(num1,num2-1)
print("%d * %d = %d" %(num1,num2,multiplica(num1,num2)))

