nome= input("Qual o seu nome ? ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
sexo = input("Digite o seu sexo: ")
imc = peso/(altura*altura)
status = ""

if (sexo == "m") | (sexo == "M"):
    if imc<=20.7 :
        status ="Abaixo do Peso"
    elif imc<=26.4:
        status = "Peso Normal"
    elif imc<=27.8:
        status = "Marginalmente acima do peso"
    elif imc<=31:
        status = "Peso Normal"
if (sexo == "f") | (sexo == "F"):
    if imc<=19.1 :
        status = "Abaixo do Peso"
    elif imc<=25.8:
        status = "Peso Normal"
    elif imc<=27.3:
        status = "Marginalmente acima do peso"
    elif imc<=32.3:
        status = "Peso Normal"

print("%s seu imc é %d e seu status é:  %s"%(nome,imc,status))
