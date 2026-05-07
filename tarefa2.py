peso = int(input("digite o peso: "))
altura = float(input("digite a altura: "))

imc = peso / (altura ** 2)

print(f"seu imc é {imc:.2f}")
if imc < 18.5: 
    print('você está abaixo do peso')
elif imc < 25:
    print('você está com o peso normal')
elif imc < 30: 
    print('você está com sobrepeso')
elif imc < 35:
    print('você está com obesidade grau 1')
elif imc < 40:
    print('você está com obesidade grau 2')
else: 
    print('você está com obesidade grau 3')
