import math
n = [30,6,9,4,2]
pulo = len(n) / 2
aux = 1
i = 0
while pulo >= 1:
    pulo = math.ceil(pulo)
    if len(n)%2 != 0 :
        tamanho = pulo-1
    while i < tamanho :
        print("Pulo %d : "%(pulo))
        if n[i] > n[i+pulo]:
            print(i)
            print(n[i])
            print(pulo)
            print(n[i+pulo])
            aux = n[i]
            n[i] = n[i + pulo]
            n[i + pulo] = aux
            print(n)
        i += 1
        if pulo == 1:
            print("Pulo %d com 1 : "%(pulo))
            i = 0
            while i < len(n)-1 :
                print("Valor %d"%(i))
                if n[i] > n[i+pulo]:
                    print("I %d  "%(i))
                    print("N[I] %d  "%(n[i]))
                    print("Pulo %d "%(pulo))
                    print("N[i+pulo] %d  "%(n[i+pulo]))
                    aux = n[i]
                    n[i] = n[i + pulo]
                    n[i + pulo] = aux
                    print(n)
                i += 1

    pulo /= 2
    i = 0
print(n)
