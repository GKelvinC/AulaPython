from datetime import date

#Variaveis
data = input("Diga sua data de nascimento")
datahj = date.today()
vetor_data = data.split("/")
anos = datahj.year - int(vetor_data[2]);
print(vetor_data)
#Calculo da IDADE
if int(vetor_data[1]) <= datahj.month :
    if int(vetor_data[1]) == datahj.month:
        if int(vetor_data[0]) >= datahj.day :
            anos = anos
        else:
            anos = anos -1
            meses = (12 - int(vetor_data[1]))+ datahj.month
    else:
        anos = anos
        meses = datahj.month - int(vetor_data[1])
else:
    anos = anos-1
    meses = 12 - int(vetor_data[1])
    if (datahj.day >= int(vetor_data[0])):
            meses = meses + datahj.month
    else:
        meses = meses + (datahj.month-1)
#Meses
if datahj.month > int(vetor_data[1]):
    if datahj.day < int(vetor_data[0]):
        print("Você tem %d anos, %d meses e %d dias"%(anos,meses,int(vetor_data[0])-datahj.day))
    else:
        print("Você tem %d anos, %d meses e %d dias"%(anos,meses,datahj.day-int(vetor_data[0])))
elif datahj.month == int(vetor_data[1]):
    if datahj.day == int(vetor_data[0]):
        print("Você tem %d anos"%(anos))
    else:
        print("Você tem %d anos e %d dias"%(anos,datahj.day))
else:
    if(datahj.month-1)== 1|3|5|7|8|10|12:
        print("Você tem %d anos, %d meses e %d dias aqui"%(anos,meses,datahj.day+(31-int(vetor_data[0]))))
    elif(datahj.month-1) == 2:
        if datahj.day > int(vetor_data[0]):
            print("Você tem %d anos, %d meses e %d dias aqui"%(anos,meses,datahj.day-int(vetor_data[0])))
        else:
            print("Você tem %d anos, %d meses e %d dias aqui"%(anos,meses,datahj.day+(28-int(vetor_data[0]))))
    elif(datahj.month-1) == 4|6|9|11:
        print("Você tem %d anos, %d meses e %d dias aqui"%(anos,meses,datahj.day+(30-int(vetor_data[0]))))
