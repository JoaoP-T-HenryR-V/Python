qntU,qnt18 = 0
user = input("Digite seu nome: ")
while user.lower() != "encerrar":
    idade = input("Digite sua idade: ")
    if idade.lower() == "encerrar":
        break
    idade = int(idade)
    qntU += 1
    if idade>=18:
        qnt18 += 1
    user = input("Digite seu nome: ")
print ("a quantidade de usuarios cadastrados é: ", qntU)
print ("a quantidade de usuarios cadastrados com 18 ou mais é: ", qnt18)