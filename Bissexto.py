ano = int(input("Digite o ano"))
if (ano % 4 == 0)&(ano % 100 != 0)|(ano % 400 == 0):
    print("Ano é bissexto")
else:
    print("Não é bissexto")
