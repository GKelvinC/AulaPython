peso=[]
altura=[]
nome=[]
imc=[]
somapesos= 0
somaaltura= 0
tot = int(input("Quantos alunos tem na turma ?"))
i = 0
nomeMenor = ''
nomeMaior = ''
imcMaior = 0
imcMenor = 0
while i < tot :
    nome.append(input("Digite seu nome: "))
    peso.append(float(input("Digite seu peso: ")))
    altura.append(float(input("Digite sua altura: ")))
    imc.append(float(peso[i]/(altura[i]*altura[i])))
    print(imc[i])
    somapesos = somapesos + peso[i]
    somaaltura = somaaltura + altura[i]
    i = i + 1
i = 0
while i <= tot-1:
    ii = 0
    while ii < tot:
        if imc[i]>imc[ii]:
            imcMaior = imc[i]
            nomeMaior = nome[i]
        if imc[i]<imc[ii]:
            imcMenor = imc[i]
            nomeMenor = nome[i]
        ii = ii + 1
    i = i + 1
mediapesos = float(somapesos/tot)
mediaaltura = float(somaaltura/tot)

print("A média dos pesos é : %d"%(mediapesos))
print("A média das alturas é : %d"%(mediaaltura))
print("O Aluno %s tem o maior imc com %d"%(nomeMaior,imcMaior))
print("O Aluno %s tem o menor imc com %d"%(nomeMenor,imcMenor))
