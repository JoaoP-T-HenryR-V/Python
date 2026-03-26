idv = input("Digite o ID do vendedor: ")
idp = int (input("Digite o ID do produto: "))
pp = float(input("Digite o preço do produto: "))
qtdv = int(input("Digite a quantidade vendida: "))
total = pp*qtdv
comission = total*0.05
print("O funcionário", idv, "vendeu", qtdv, "do id", idp, "e ganhou", total, "para empresa, sua comissão será de", comission)