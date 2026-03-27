i = float(input("Digite uma Nota: "))
maior,menor,media = i
qtd = 1
if i != -1:
    while i != -1:
        i = float(input("Digite uma Nota: "))
        media += i
        if i > maior:
            maior = i   
        if i < menor:
            menor = i   
        qtd += 1
media = media/qtd
print ("A maior nota foi:", maior)
print ("A menor nota foi:", menor)
print ("A média das notas foi:", media)