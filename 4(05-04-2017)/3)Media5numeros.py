i = 0
nota = []
while i < 5:
    nota.append(int(input("Digite o %dº numero: "%(i+1))))
    i = i + 1

soma = nota[0]+nota[1]+nota[2]+nota[3]+nota[4]
media = (nota[0]+nota[1]+nota[2]+nota[3]+nota[4])/5

print("A soma desses 5 numeros é : %d "%(soma))
print("A média desses 5 numeros é : %d "%(media))
