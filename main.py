def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b

def menu():
    print("\n=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

def main():
    while True:
        menu()

        opcao = input("Escolha uma operação: ")

        if opcao == "0":
            print("Encerrando...")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida!")
            continue

        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            continue

        try:
            if opcao == "1":
                resultado = somar(a, b)
            elif opcao == "2":
                resultado = subtrair(a, b)
            elif opcao == "3":
                resultado = multiplicar(a, b)
            elif opcao == "4":
                resultado = dividir(a, b)

            print(f"Resultado: {resultado}")

        except Exception as e:
            print(f"Erro: {e}")

main()