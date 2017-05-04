numero = int(input("Digite um numero"))
n=[1,1]
aux = n[0]+n[1]
while aux <= numero :
    n.append(aux)
    aux = n[len(n)-1]+n[len(n)-2]
print(n)
