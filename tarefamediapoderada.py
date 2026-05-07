n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

print("1 - Média ponderada")
print("2 - quadrado da soma de 2 numeros")
print("3 - cubo do menor numero")
opcao = int(input("digite uma opção: "))

if opcao == 1:
    resultado = (n1 * 2 + n2 * 3) / 5
    print(f"O resultado é {resultado}")
          
elif opcao == 2:
    resultado = (n1 + n2) ** 2 
    print(f"O resultado é {resultado}")
          
elif opcao == 3:
    menor = n1 if n1 < n2 else n2
    resultado = menor ** 3     
    print(f"O resultado é {resultado}")

else: 
    print("opção invalida")
