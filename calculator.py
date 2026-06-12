from os import system
from time import sleep
system('cls')

def clearConsole():
    system('cls')

def calculator(option, n1, n2):
    package = {
        "operacao": "",
        "resultado": 0,
        "error": ""
    }
    try:
        match option:
            case "1":
                package["operacao"], package["resultado"] = "soma", n1 + n2
            case "2":
                package["operacao"], package["resultado"] = "subtracao", n1 - n2
            case "3":
                package["operacao"], package["resultado"] = "multiplicar", n1 * n2
            case "4":
                package["operacao"], package["resultado"] = "dividir", n1 / n2
            case "5":
                package["operacao"], package["resultado"] = "resto de divisao", n1 % n2
            case _:
                package["error"] = "NotExistsThisOption"
    except ZeroDivisionError:
        package["error"] = "ZeroDivision"
    except Exception as e:
        package["error"] = f"internal error\n{str(e)}"

    return package

def init():
    while True:
        clearConsole()
        print("Bem vindo a calculadora da resenha")
        print("resenhe suas operações aritméticas aqui\n")
        try:
            firstNumber = float(input("Informe o primeiro número: "))
            secondNumber = float(input("Informe o segundo número: "))
        except ValueError:
            print("Pofavor insira apenas Números")
            continue

        clearConsole()

        option = input(f"""
1.Soma
2.Subtrair
3.Multiplicar
4.Dividir
5.Resto de divisão
6.Sair\n
Números inseridos:\nPrimeiro: {firstNumber}\nSegundo: {secondNumber}\n
Insira a opção: """)
        
        clearConsole()

        if option == "6":
            print("Adeus ...")
            sleep(1.5)
            break
        else:
            print("Calculando o Resultado .....")
            resultado = calculator(option, firstNumber, secondNumber)
            if resultado["error"]:
                match resultado["error"]:
                    case "NotExistsThisOption":
                        print("essa opção não existe\nporfavor selecionar outra opção")
                    case "ZeroDivision":
                        print("não e possivel realizar divisão com zero\npofavor não insira o número zero")
                    case _:
                        print(f"INTERNAL ERROR\n{resultado["error"]}")
                
                sleep(2.5)
                clearConsole()
                print("Voltando ao inicio ...")
                sleep(1.5)
                continue
        sleep(1)
        clearConsole()

        input(f"""
========================================================
    Números inseridos: [ 1 = {firstNumber:.2f} / 2 = {secondNumber:.2f} ]
    Operação Selecionada: ( {resultado["operacao"]} )
    Resultado: {resultado["resultado"]:.2f}

    pra voltar ao menu pressione qualquer botão ...
========================================================
            """)
        
if __name__=="__main__":
    init()
