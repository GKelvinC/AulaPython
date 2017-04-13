v=[]
vn=[]
n = 0
while n < 10:
    v.append(int(input("Digite o %dº numero : "%(n+1))))
    n = n +1
n = 9
while n > -1 :
    vn.append(v[n])
    n = n -1
print(v)
print(vn)
