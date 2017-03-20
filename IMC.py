peso = float(input("Diga qual o seu peso: "))
altura = float(input("Diga qual a sua altura: "))
sexo = input("Qual o seu sexo ?(M/F)")
imc = peso/(altura*altura)
if (sexo == "F" )|(sexo == "f"):
    if (imc <= 19.1):
        situ = "Abaixo do peso"
    elif (imc <= 25.8):
        situ = "Peso Normal"
    elif (imc <= 27.3):
        situ = "Marginalmente Acima do Peso"
    elif (imc <= 32.3):
        situ = "Acima do peso ideal"
elif (sexo == "M" )|(sexo == "m"):
    if (imc <= 20.7):
        situ = "Abaixo do peso"
    elif (imc <= 26.4):
        situ = "Peso Normal"
    elif (imc <= 27.8):
        situ = "Marginalmente Acima do Peso"
    elif (imc <= 31):
        situ = "Acima do peso ideal"
print("Seu imc é: %2.2f"%imc)
print("Sua situação é: %s " %situ)