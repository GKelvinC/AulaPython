v=[]
impar=[]
par=[]
n = 0
while n < 10:
    v.append(int(input("Digite o %dº numero : "%(n+1))))
    n = n +1
n = 0
while n < 20:
    if v[n]%2 == 0:
        par.append(v[n])
    else :
        impar.append(v[n])
    n = n + 1
print("Vetor Orgiginal",v)
print("Vetor Impar",impar)
print("Vetor Par",par)
