##Levando em conta cada mês com 30 dias e o ano com 360 dias

dias = int(input("Quantos dias de vida você tem?"))
anos = int(dias/360)
dias_restantes = dias-(360*anos)
meses = int(dias_restantes/30)
dias_restantes2 = dias_restantes-(30*meses)
print("Voce tem %d anos , %d meses , %d dias de vida "%(anos,meses,dias_restantes2))
