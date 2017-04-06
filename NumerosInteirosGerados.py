import random
n1= -1
n2= -1
while (n1 and n2) < 0 :
    n1 = float(input("Digite o 1º numero :"))
    n2 = float(input("Digite o 2º numero :"))

aleatorio = random.randint(n1,n2)
print("O numero aleatorio é : %d"%(aleatorio))

