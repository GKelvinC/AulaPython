cigarros = int(input("Quantos cigarros você fuma por dia ?"))
anos = int(input("Há quantos anos você fuma ?"))
anos = anos * 365 #Anos em dias
minutosTotais = (cigarros*10)*anos #minutos totais perdidos
total = minutosTotais/1440 #minutos totais
print("Dias de vida perdidos %d"%(total))


