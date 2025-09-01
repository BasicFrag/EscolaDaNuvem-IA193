"""
Crie um programa que verifique se uma senha é forte. 
Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. 
O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.

"""

while True:
    entrada = input("Digite sua senha!\n")
    caracteres_especiais = "!@#$%&*"
    contador_alfabetico = 0
    contador_numerico = 0
    contador_especial = 0
    contador_maiuscula = 0

    if entrada == "sair":
            print("Nenhuma senha foi inserida. Até mais!")
            break
    if len(entrada) < 8:
            print("A senha deve ter no mínimo 8 caracteres")
            continue
    else:
        for char in entrada:
            if char.isdigit():
                contador_numerico += 1
            elif char.isalpha():
                contador_alfabetico +=1
                if char == char.upper():
                    contador_maiuscula += 1
            elif any(char == especial for especial in caracteres_especiais):
                    contador_especial +=1
        
    if contador_numerico == 0:
        print("É necessário pelo menos um digito! Tente novamente!")
        continue
    if contador_alfabetico == 0:
        print("É necessário pelo menos um letra minúscula! Tente novamente!")
        continue
    if contador_maiuscula == 0:
        print("É necessário pelo menos uma letra maiuscula! Tente novamente!")
        continue
    if contador_especial == 0:
        print("É necessário pelo menos um caracter especial! Tente novamente!")
        continue
    print(f"Caracteres alfabéticos: {contador_alfabetico}, maiúsculos: {contador_maiuscula}, números: {contador_numerico} e especiais: {contador_especial}")
    print("Senha forte!")
    break