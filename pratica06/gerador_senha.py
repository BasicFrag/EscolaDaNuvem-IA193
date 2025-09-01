import random
import string

def gerador_senha(tamanho):
    caracteres = string.ascii_letters + "!@#$%&*"
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha

print(gerador_senha(10))