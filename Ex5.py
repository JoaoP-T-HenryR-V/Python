salarioA = float(input ("Coloque seu salario atual: "))
if salarioA >= 0:
    if salarioA <1000.01:
        salarioB = salarioA * 1.2
    elif salarioA < 5000.01:
        salarioB = salarioA * 1.1
    else:
        salarioB = salarioA * 1.05
    print ("Seu novo salario é de: ", salarioB)
else:
    print ("Salario invalido")
    