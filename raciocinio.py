p = True
q = True
r = True

# Função contendo toda a logica
def calculo_expre(p, q, r):
    # (q ^ r)
    if p & r is True:
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
    if p is True: p = 'True '
    if q is True: q = 'True '
    if r is True: r = 'True '
    if q1 is True: q1 = 'True '
    if p1 is True: p1 = 'True '
    if p2 is True: p2 = 'True '
    if p3 is True: p3 = 'True '
    if qF is True: qF = 'True '
    if Result is True: Result = 'True '

    return [p, q, r, q1, p1, p2, p3, qF, Result]

#Função para imprimir
def imprimir_tela(vt):
    print("| %s | %s | %s |  %s    |    %s      |   %s   |   %s   |         %s         |        %s" % (vt[0], vt[1], vt[2], vt[3], vt[4], vt[5], vt[6], vt[7], vt[8]))

print("Expressão: p v ( q ^ r ) <--> ( p v q )^ ( p v r )")
print("---------------------------------------------------------------")
print("|   p   |   q   |   r   | ( q ^ r ) | p v ( q ^ r ) | ( p v q ) | ( p v r ) | ( p v q ) ^ ( p v r ) | p v ( q ^ r ) <--> ( p v q )^ ( p v r )")

# Loop que monta a tabela
i = 1
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

