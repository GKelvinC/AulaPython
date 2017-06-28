linhas=int(input("Informe o numero de linhas: "))
colunas=int(input("Informe o numero de colunas: "))
desafio =[0]*linhas

print(desafio)
for i in range(linhas):
    desafio[i]=[0]*colunas

print("="*10,"Forma Raiz","="*10)
print(desafio)

print("="*10,"Forma Bonita","="*10)
for i in range(linhas):
    print(desafio[i])