deseja = input("Deseja imprimir a tabela com todos os valores ?(V/F)")
if deseja == "V":
    p = True
    q = True
    r = True
else:
    p = input("Digite o valor de P: ( V/F)")
    if p == "V" :
        p = True
    else:
        p = False
    q = input("Digite o valor de Q: ( V/F)")
    if q == "V" :
        q = True
    else:
        q = False
    r = input("Digite o valor de R: ( V/F)")
    if r == "V" :
        r = True
    else:
        r = False
    ii = 2
# Função contendo toda a logica
def calculo_expre(p, q, r):
    # (q ^ r)
    if q & r is True:
        q1 = True
    else:
        q1 = False

    # p v ( q ^ r )
    if p & q1 is False:
        p1 = False
    else:
        p1 = True

    # ( p v q )
    if p & q is False:
        p2 = False
    else:
        p2 = True

    # ( p v r )
    if p & r is False:
        p3 = False
    else:
        p3 = True

    # ( p v q ) ^ ( p v r )
    if p2 & p3 is True:
        qF = True
    else:
        qF = False

    # p v ( q ^ r ) <--> ( p v q )^ ( p v r )
    if p1 != qF:
        Result = False
    else:
        Result = True
        # -------------- Fim Lógica -------
    # --- Usado somente para melhorar o design da tabela pois true tem menos caracteres que o false
    if p is True: p = '  V  '
    if q is True: q = '  V  '
    if r is True: r = '  V  '
    if q1 is True: q1 = '  V  '
    if p1 is True: p1 = '  V  '
    if p2 is True: p2 = '  V  '
    if p3 is True: p3 = '  V  '
    if qF is True: qF = '  V  '
    if Result is True: Result = '  V  '

    if p is False: p = '  F  '
    if q is False: q = '  F  '
    if r is False: r = '  F  '
    if q1 is False: q1 = '  F  '
    if p1 is False: p1 = '  F  '
    if p2 is False: p2 = '  F  '
    if p3 is False: p3 = '  F  '
    if qF is False: qF = '  F  '
    if Result is False: Result = '  F  '


    return [p, q, r, q1, p1, p2, p3, qF, Result]
#Função para imprimir
def imprimir_tela(vt):
    print("| %s | %s | %s |  %s    |    %s      |   %s   |   %s   |         %s         |        %s" % (vt[0], vt[1], vt[2], vt[3], vt[4], vt[5], vt[6], vt[7], vt[8]))
#Função que mostra a resolução do problema
def resolucao(vt):
    print(" ")
    print ( "RESOLUÇÃO:" )
    print ( "---1ºParte da Resolução: \n   Divida a expressão em partes \n                                             1º Parte : p v ( q ^ r ) / 2º Parte : ( p v q ) ^ ( p v r )  \n    Solucione primeiro os parenteses: " )
    print ( "    (q ^ r ) = %s /Explicação : Numa conjunção ( ^ ) , o resultado é verdadeiro somente quando os dois lados são verdadeiros "%(vt[3]))
    input ("    Vamos Prosseguir?(Pressione qualquer tecla!)")
    print(" ")
    print ( "---2ºParte da Resolução: \n   Sabendo que ( q ^ r ) é %s resolvemos a 2º parte: "%(vt[3]))
    print ("     p v (q ^ r ) = %s /Explicação : Numa disjunção ( v ) , o resultado é falso somente quando os dois lados são falsos " % (vt[4]))
    input ("     Vamos Prosseguir?(Pressione qualquer tecla!)")
    print(" ")
    print ( "---3ºParte da Resolução: \n   Resolvemos a segunda parte que e começamos com o ( p v q ): ")
    print ("     ( p v q ) = %s /Explicação : Numa disjunção ( v ) , o resultado é falso somente quando os dois lados são falsos " % (vt[5]))
    input ("    Vamos Prosseguir?(Pressione qualquer tecla!)")
    print(" ")
    print ( "---4ºParte da Resolução: \n   Após resolver o primeiro parenteses viermos resolver o segundo, ( p v r ): ")
    print ("     ( p v r ) = %s /Explicação : Numa disjunção ( v ) , o resultado é falso somente quando os dois lados são falsos " % (vt[6]))
    input ("    Vamos Prosseguir?(Pressione qualquer tecla!)")
    print(" ")
    print ( "---5ºParte da Resolução: \n   Após resolver os parenteses agora resolvemos toda a 2º parte, ( p v q ) ^ ( p v r ): ")
    print ("     ( p v q ) ^ ( p v r ) = %s /Explicação : Numa conjunção ( ^ ) , o resultado é verdadeiro somente quando os dois lados são verdadeiros " % (vt[7]))
    input ("    Vamos Prosseguir?(Pressione qualquer tecla!)")
    print(" ")
    print ( "---Resultado Final: \n   Após resolver ambas as partes Resolvemos a ultima parte, p v ( q ^ r ) <--> ( p v q )^ ( p v r ): ")
    print ("     p v ( q ^ r ) <--> ( p v q )^ ( p v r ) = %s /Explicação : Numa Bi-Condição ( <--> ) , \n o resultado é verdadeiro somente quando ambas as opções forem iguais ( Ex: F e F OU V e V ) " % (vt[8]))
    print ( " " )
#Função que mostra a expressão a ser resolvida
def expressao():
    print("Expressão: p v ( q ^ r ) <--> ( p v q )^ ( p v r )")
    print("---------------------------------------------------------------")
    print("|   p   |   q   |   r   | ( q ^ r ) | p v ( q ^ r ) | ( p v q ) | ( p v r ) | ( p v q ) ^ ( p v r ) | p v ( q ^ r ) <--> ( p v q )^ ( p v r )")
#IF que decide se Monta uma tabela intera ou somente uma linha
if deseja != "V":
    vt = calculo_expre ( p, q, r )
    resolucao(vt)
    expressao ()
    imprimir_tela ( vt )
else:
    # Loop que monta a tabela
    i = 1
    expressao()
    while i < 9:
        if i == 2:
            q = False
            r = False
        if i == 3 or i == 8:
            q = True
            r = False
        if i == 4 or i == 7:
            q = False
            r = True
        if i == 5:
            p = False
            q = False
            r = False
        if i == 6:
            q = True
            r = True
        vt = calculo_expre(p, q, r)
        imprimir_tela(vt)
        i += 1
finalizar = input("Deseja finalizar o programa ?")

