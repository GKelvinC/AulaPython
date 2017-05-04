import random
erros=0
nomes=["lua","sol","dia"]
forca=[]
posi = random.randrange(0,len(nomes))
palavra= nomes[posi]
tamanhodapalavra = len(palavra)
print(palavra)
print(tamanhodapalavra)
i = 1

palavraAn = "_"
while i < tamanhodapalavra:
    palavraAn += "_"
    i += 1
print(palavraAn)

letra=input("Digite uma letra")

if palavra.find(letra) < 0 :
    erros = erros +1
else:
    posiletra = palavra.find(letra)
    print(posiletra)
    if posiletra != 0 :
        novaPalavraAn = palavraAn[:posiletra]+letra+palavraAn[posiletra:]
    print(novaPalavraAn)
    print('_ i _')

