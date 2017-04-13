l=[]
n = 0
while n < 3:
    l.append(int(input("Qual é o valor do %dº Lado"%(n+1))))
    n = n +1
if (l[0] == l[1]) & (l[1]==l[2]):
    print("Triangulo Equilátero")
elif (l[0] == l[1]) | (l[0]==l[2]) | (l[1]==l[2]):
    print("Triângulo Isosceles")
elif (l[0] != l[1]) & (l[0] != l[2]) & (l[1] != l[2]) :
    print("Triângulo Escaleno")

