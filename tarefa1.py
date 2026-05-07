valor=int(input("digite o valor: "))
print("1 - vista 15%")
print("2 - debito 10%")
print("3 - credito 5%")
opcao=int(input("digite uma opcao: "))
if opcao==1:
    desconto= valor*15/100
    final= valor - desconto
    print (f"seu desconto é: {final}")

elif opcao==2:
    desconto= valor*10/100
    final= valor - desconto
    print (f"seu desconto é: {final}")

elif opcao==3:
    desconto= valor*5/100
    final= valor - desconto

    print (f"seu desconto é: {final}")

else: print(f"opção invalida")


