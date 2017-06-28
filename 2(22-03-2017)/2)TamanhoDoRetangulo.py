base=int(input("digite o valor da base:"))
altura=int(input("digite o valor da altura:"))
result=base*altura
if base==altura:
    print("Esse é um quadrado, e sua área é igual a:",result,"cm²")
else:
    print("Esse é um retangulo, e sua área é igual a:",result,"cm²")