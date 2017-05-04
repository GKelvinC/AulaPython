valor_a_ser_pago = int(input("Digite o valor a ser pago"))
valorRecebido = int(input("Digite o valor Recebido"))
troco = valorRecebido - valor_a_ser_pago
notas=[50,20,10,5,2,1]
quant=[0,0,0,0,0,0]
print(troco)
i = 0
while i < len(notas):
    aux = 0
    while troco >= notas[i]:
        troco -= notas[i]
        aux = quant[i]
        aux += 1
        quant[i] = aux
    i +=1

print(troco)
print("O caixa deve pegar %d notas de 50"%(quant[0]))
print("O caixa deve pegar %d notas de 20"%(quant[1]))
print("O caixa deve pegar %d notas de 10"%(quant[2]))
print("O caixa deve pegar %d notas de 5"%(quant[3]))
print("O caixa deve pegar %d notas de 2"%(quant[4]))
print("O caixa deve pegar %d notas de 1"%(quant[5]))

