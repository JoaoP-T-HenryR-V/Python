senha = "adm123"
email = "adm123"
for i in range(1,4):
    emailU = input("Digite seu email: ")
    senhaU = input("Digite sua senha: ")
    if senhaU == senha and emailU == email:
        print("Login feito com sucesso!")
        break
    else:
        print("Senha ou Email incorreto.")
        if i>=3:
            print("Conta Bloqueada")
            break
            

