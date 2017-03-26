n = []
n1 = []
want = "y"
cont = 0
i = 0
aux = 0
tamN = 0
while want == "y":
    n.append(int(input("Write a number : ")))
    want = input("You want write more numbers ? ")
    cont = cont + cont
print(n)
aux2 = len(n)
tamN = len(n)
while len(n1) != aux2:
    while i < tamN:
        cont1 = 0
        print("N[i]: %d" % (i))
        for ii in range(0, tamN):
            print("N[i]: %d  e N[ii]: %d e tam N %s" % (n[i], n[ii], len(n)))
            print(" ")
            if n[i] <= n[ii]:
                cont1 = cont1 + 1
        print(cont1)
        print(len(n))
        if cont1 == len(n):
            n1.append(n[i])
            n.remove(n[i])
            print(n1)
            print(n)
            print("N1 tam :%d" % (len(n1)))
            print("N tam :%d" % (len(n)))
            tamN = len(n)
            i = 0
        else:
            i = i + 1