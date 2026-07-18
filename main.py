from operacoes import *

# Visualização inicial do programa.

while True:

    print("\n======================")
    print("    CALCULADORA HC 1.0")
    print("======================")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Potência")
    print("6 - Raiz Quadrada")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "0":
        print("Até logo!")
        break

# Como o programa funciona:

    try:

        if opcao == "6":
            numero = float(input("Digite um número: "))
            print(f"\nResultado: {raiz(numero)}")

        elif opcao in ["1", "2", "3", "4", "5"]:

            n1 = float(input("Primeiro número: "))
            n2 = float(input("Segundo número: "))

            if opcao == "1":
                print(f"\nResultado: {somar(n1, n2)}")

            elif opcao == "2":
                print(f"\nResultado: {subtrair(n1, n2)}")

            elif opcao == "3":
                print(f"\nResultado: {multiplicar(n1, n2)}")

            elif opcao == "4":
                print(f"\nResultado: {dividir(n1, n2)}")

            elif opcao == "5":
                print(f"\nResultado: {potencia(n1, n2)}")

        else:
            print("\nOpção inválida!")

    except ValueError:
        print("\nDigite apenas números.")