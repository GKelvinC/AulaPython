tamanho = float(input("Digite o tamanho em metros quadrados:"))
litrosNecessario = tamanho/3
Latas= litrosNecessario/18
if Latas - int(Latas) > 0:
    Latas = int(Latas)+1
print("Quantidade de latas : %d "%(Latas))
print("Preço total: R$ %d"%(Latas*80))
