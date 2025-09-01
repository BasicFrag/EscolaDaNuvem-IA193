"""
Crie um programa que permita a um professor registrar as notas de uma turma. 
O programa deve continuar solicitando notas até que o professor digite 'fim'. 
Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma

"""

contador = 0
notas = 0


while True:
    try:
        entrada = input("Digite uma nota de 0 a 10: ")
        if entrada.lower() == "fim":
             break
        if (float(entrada) < 0 or float(entrada) > 10):
            print("Somente números entre 0 e 10!")
            continue
        notas += float(entrada)
        contador += 1
        print(notas)
    except ValueError:
        print("Entrada inválida!")
if notas == 0:
    print("Nenhuma nota inserida. Até mais!")
else:
    print("Média final:", round((notas / contador),1))
