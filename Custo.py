valor_do_carro = int(input("Qual o custo de fabrica do veiculo ?"))
TaxaDistribuidor = (valor_do_carro * 28)/100
TaxaImpostos = (valor_do_carro * 45)/100
valor_do_carro = valor_do_carro+TaxaDistribuidor+TaxaImpostos
print("O valor do carro é : R$ %d "%(valor_do_carro))
