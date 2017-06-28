qnt = int(input("Quantidade de idades a serem calculadas: "))
idade=[]
for i in range (qnt):
    idade.append(int(input("Informe a idade: ")))
    if i == 0:
        menor = int(idade[i])
        maior = int(idade[i])
    if idade[i] > maior:
        maior = idade[i]
    if idade[i] < menor:
        menor = idade[i]
print("Maior número digitado: %d"%maior)
print("Menor número digitado: %d"%menor)