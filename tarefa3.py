from math import sqrt

x1 = float(input(" digite x1: "))
y1 = float(input(" digite y1: "))

x2 = float(input(" digite x2: "))
y2 = float(input(" digite y2: "))

distancia = sqrt((x2 - x1)**2) + sqrt((y2 - y1)**2)

print(f"A distância entre os pontos é: {distancia:.2f}")