base = int(input("Diga a base: "))
altura = int(input("Diga a altura: "))
poligono = ""
area = base * altura
if(base == altura):
    poligono = "quadrado"
else:
    poligono ="retangulo"
print("A area do %s é %d"%(poligono,area))
