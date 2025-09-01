"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). 
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""

def teste_palindromo(palavra: str):
    palavra_limpa = "".join(char.lower() for char in palavra if char.isalnum())
    palavra_reversa = palavra_limpa.strip().lower()[::-1]
    is_palindromo = palavra_limpa == palavra_reversa
    # print(palavra_reversa, palavra_limpa)
    return is_palindromo
    
palavra = input("Digite uma palavra ou frase: \n")

if teste_palindromo(palavra):
    print(palavra, "é um palíndromo!")
    print(teste_palindromo(palavra))
else:
    print(palavra, "não é um palídromo")