"""5- Calculadora de Soma com Entrada do Usuário

Leia 2 valores inteiros e armazene-os nas variáveis A e B. 

Efetue a soma de A e B, atribuindo o seu resultado à variável X. 

Entrada: A entrada contém 2 valores inteiros informados pelo usuário. 

Saída: Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha."""

numero_inteiro_A: int = int(input("Digite o valor de A: "))
numero_inteiro_B: int = int(input("Digite o valor de B: "))
resultado_X = numero_inteiro_A + numero_inteiro_B
print(f"X = {resultado_X}")