altura = float(print("Digite sua altura: "))
peso = float(print("Digite seu peso: "))
imc = peso/(altura*altura)
if imc < 18.5:
    print("abaixo do peso normal")
elif imc >= 18.5 and imc < 24.9:
    print("peso normal")
elif imc >= 25 and imc < 30:
    print("acima do peso")
elif imc >= 30 and imc < 35:
    print("obesidade classe I")
elif imc >= 35 and imc < 40:
    print("obesidade classe II")
elif imc < 40:
    print("obesidade classe III")