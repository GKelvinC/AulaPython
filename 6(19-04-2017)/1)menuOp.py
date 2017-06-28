def l():
    print()

def lernumeros():
    a=int(input("Digite um número: "))
    b=int(input("Digite um número: "))
    c=int(input("Digite um número: "))
    return(a,b,c)

def soma(a,b,c):
    s=(a+b+c)
    print("A Soma dos números é: ",s)

def maior(a,b,c):
    if a>b and a>c:
        print("O Maior número é: ",a)
    elif b>a and b>c:
        print("O Maior número é: ",b)
    else:
        print("O Maior número é: ",c)

def menor(a,b,c):
    if a<b and a<c:
        print("O Menor número é: ",a)
    elif b<a and b<c:
        print("O Menor número é: ",b)
    else:
        print("O Menor número é: ",c)

def media(a,b,c):
    med=((a+b+c)/3)
    print("A Média dos três números é: ",med)

def op(a):
    if a==1:
        soma(n1,n2,n3)
    elif a==2:
        maior(n1,n2,n3)
    elif a==3:
        menor(n1,n2,n3)
    elif a==4:
        media(n1,n2,n3)
    else:
        print("Opção inválida :c ")

loop=1
while loop>0:
    continuar=loop

    if continuar==1:
        (n1,n2,n3)=lernumeros()
        opcao=int(input("Selecione uma das opções = Soma digite [1] - Maior [2] - Menor [3] - Média [4]: "))
        while opcao<1 or opcao>4:
            opcao=int(input("Opção Errada! Selecione uma nova opção = Soma digite [1] - Maior [2] - Menor [3] - Média [4]: "))
        l()
        op(opcao)
        continuar=int(input("Deseja realizar o processo novamente? [ Digite[Número Negativo]~Fim Programa~/ Digite[1]~Reseta os valores e reiniciar o programa~ / Digite[2]~Reinicia o programa e mantém os valores~ ]: "))
        loop=continuar
        l()

    elif continuar==2:
        opcao=int(input("Selecione uma das opções = Soma digite [1] - Maior [2] - Menor [3] - Média [4]: "))
        while opcao<1 or opcao>4:
            opcao=int(input("Opção Errada! Selecione uma nova opção = Soma digite [1] - Maior [2] - Menor [3] - Média [4]: "))
        l()
        op(opcao)
        continuar=int(input("Deseja realizar o processo novamente? [ Digite[Número Negativo]~Fim Programa~/ Digite[1]~Reseta os valores e reiniciar o programa~ / Digite[2]~Reinicia o programa e mantém os valores~ ]: "))
        loop=continuar

    else:
        loop=int(input("Opção Errada! [ Digite[Número Negativo]~Fim Programa~/ Digite[1]~Reseta os valores e reiniciar o programa~ / Digite[2]~Reinicia o programa e mantém os valores~ ]: "))
        l()
