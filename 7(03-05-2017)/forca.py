def pergunta():
    let=input("Informe uma letra: ")
    return let
def pulaL():
    print()
def enfeite1():
    print("=" * 69)
def enfeite2():
    print("-" * 69)

import random
repositorio=["abaixo","acima","boca","cola","trave","abacate","luta","queijo","prato"]
    #Escolha aleatoria da palavra pro Jogo
palavra=repositorio[random.randint(0,(len(repositorio)-1))]
    #Declaração de Vetores
palavraVet=[]
espelhoVet=[]
    #Declaração de Variaveis
tentativas=0
erro = 0
repitida = 0
acerto = 0
print(palavra) #Pra testar o jogo

#Tela Inicial
print("=-="*10,"Bem Vindo ao Jogo da Forca","=-="*10)
print("Dica: A palavra selecionada possui %d letras"%(len(palavra)))
print("=-="*12,"Agora é com você!","=-="*11)
pulaL()

for i in range(len(palavra)):
        palavraVet.append(palavra[i])
for i in range(len(palavra)):
        espelhoVet.append("_")
while tentativas <8:
    if palavraVet == espelhoVet:
        pulaL()
        pulaL()
        print("=" * 69)
        print("-"*13,"Você acertou <o/ Parabéns","-"*30)
        print("A palavra descoberta é: ",(palavra))
        enfeite2()
        enfeite1()
        break
    letra=pergunta()

    for i in range(len(palavra)):
        if espelhoVet[i] == letra:  #Se a letra ja tiver sido digitada vai ser erro
            repitida = repitida + 1

        elif palavraVet[i] == letra: #Se a letra não tiver sido digitada e estiver no jogo é ACERTO!
            espelhoVet[i] = letra
            acerto = acerto + 1

        elif palavraVet[i] != letra: # Se a letra digita não estiver na forca
            erro = erro + 1

    if repitida > 0:
        tentativas = tentativas + 1
        pulaL()
        print("="*15, "Letra já digitada Anteriormente!","="*20)
        print("(%d) tentativas utilizadas de (7) tentativas disponiveis." % tentativas)
        pulaL()
        print("A forca nesse momento está assim: ")
        print(espelhoVet)
        enfeite1()
        pulaL()


    elif acerto > 0:
        pulaL()
        print("="*15,"Letra digitada Correta!","="*29)
        print("(%d) tentativas utilizadas de (7) tentativas disponiveis." % tentativas)
        pulaL()
        print("A forca nesse momento está assim: ")
        print(espelhoVet)
        enfeite1()
        pulaL()

    elif erro > 0 :
        tentativas = tentativas + 1
        pulaL()
        print("="*15,"Letra digitada Incorreta!","="*27,"\nA letra digitada não está presente na Forca.",)
        print("(%d) tentativas utilizadas de (7) tentativas disponiveis." % tentativas)
        pulaL()
        print("A forca nesse momento está assim: ")
        print(espelhoVet)
        enfeite1()
        pulaL()
    erro = 0
    repitida = 0
    acerto = 0

if tentativas >6:
    print("="*15,"Fim de Jogo </3","="*30)
    print("Seu progesso no jogo estava assim: \n",(espelhoVet))
    print("A resposta era: ",(palavra))
    enfeite1()