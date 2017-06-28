print("Digite três números aleatórios")
n1=int(input("Insira um número:"))
n2=int(input("Insira um número:"))
n3=int(input("Insira um número:"))
if n1==n2 & n2==n3:
    print("iguais")
else:
    if n1<n2 & n2<n3:
        print("Os números inseridos foram:",n1,n2,n3)
    elif n1<n3 & n3<n2:
        print("Os números inseridos foram:",n1,n3,n2)
    elif n2<n1 & n1<n3:
        print("Os números inseridos foram:",n2,n1,n3)
    elif n2<n3 & n3<n1:
        print("Os números inseridos foram:",n2,n3,n1)
    elif n3<n1 & n1<n2:
        print("Os números inseridos foram:",n3,n1,n2)
    else:
        print("Os números inseridos foram:",n3,n2,n1)