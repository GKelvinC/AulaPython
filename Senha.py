senha = "a"
usuario = "a"
while senha == usuario:
    usuario = input("Digite o nome de usuario :  ")
    senha = input("Digite sua senha: ")
    if senha == usuario:
        print("A senha não pode ser igual a o nome de usuario")
print("Cadastrado com sucesso!!")

