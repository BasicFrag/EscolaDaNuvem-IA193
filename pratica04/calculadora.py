"""
O enunciado das atividades estão nos slides da Aula 08.

    Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:


        A calculadora deve solicitar ao usuário que insira dois números e uma operação.

        As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).

        O programa deve continuar solicitando entradas até que uma operação válida seja concluída.

        Trate os seguintes erros:

            Entrada inválida (não numérica) para os números

            Divisão por zero

            Operação inválida



        Use try/except para capturar e tratar os erros apropriadamente.

        Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.

        Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.

"""


while True:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (+, -, *, /): ").strip()
        resultado = 0
        if operacao == "+":
            resultado = numero1 + numero2
        elif operacao == "-":
            resultado = numero1 - numero2
        elif operacao == "*":
            resultado = numero1 * numero2
        elif operacao == "/":
            resultado = numero1 / numero2
        else:
            raise TypeError("Operação inválida. Tente novamente")
        print(resultado)
        break    
    except ValueError:
        print("Entrada inválida! Tente novamente")
    except TypeError as e:
        print(e)
    except ZeroDivisionError:
        print("Divisão por zero não é possível! Tente novamente")