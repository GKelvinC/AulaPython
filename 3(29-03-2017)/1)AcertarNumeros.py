def pulalinha():
    print()

num = int(input("Digite um número de 0 a 10: "))
while num <0 or num >10:
    pulalinha()
    print("=" * 20, " Número Incorreto! ", "=" * 20)
    num = int(input("Digite um número de 0 a 10: "))
    print("=" * 61)

chute = 20
t = 0
print ("\n" * 130)

while chute!=num:
    t = t+1
    chute = int(input("Digite seu chute: "))
    if chute > num:
        pulalinha()
        print("Erroww! Chutou muito pra cima fera")
    elif chute < num:
        pulalinha()
        print("Erroww! Chutou muito pra baixo fera")
    else:
        pulalinha()
        print("=" * 20, " Fim de Jogo ", "=" * 20)
        print("Acertou Mizeravi!!")
        print("Número total de tentativas: ",t)
        print("=" *55)