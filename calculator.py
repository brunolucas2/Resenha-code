from os import system
from time import sleep
system('cls')
def init():
    n1 = float(input("Infomre o primeiro número: "))
    n2 = float(input("Infomre o segundo número: "))
    result = 0.0
    system('cls')
    while True:
        option = input(f"1.Soma\n2.Subtrair\n3.Multiplicar\n4.Dividir\n5.Resto de divisão\n6.Sair\n\nNúmeros:\nPrimeiro: {n1}\nSegundo: {n2}\n\nOpção escolhida: ")
        system('cls')
        print("Calculando o Resultado .....")
        sleep(1)
        match option:
            case "1":
                result = n1 + n2
                break
            case "2":
                result = n1 - n2
                break
            case "3":
                result = n1 * n2
                break
            case "4":
                result = n1 / n2
                break
            case "5":
                result = n1 % n2
                break
            case "6":
                system('cls')
                print("Adeus")
                break
    
    system('cls')
    if result:
        print(result)

if __name__=="__main__":
    init()
