nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3)/3
if media >= 8:
    print("Conceito = A")
elif media >= 5:
    print("Conceito = B")
elif media < 5:
    print("Conceito = C")