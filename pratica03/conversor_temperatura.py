"""
4- Conversor de Temperatura 

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

"""

temperatura_entrada = float(input("Digite a sua temperatura: "))
temperatura_convertida = 0

escala_entrada = input("Digite a escala de entrada: Celsius, Fahrenheit ou Kelvin (ou C, F ou K): ").upper()
escala_saida = input("Digite a a escala de saída: Celsius, Fahrenheit ou Kelvin (ou C, F ou K): ").upper()

while escala_entrada == "" or escala_saida == "" :
    escala_entrada = input("Digite a escala de entrada: Celsius, Fahrenheit ou Kelvin (ou C, F ou K): ").upper()
    escala_saida = input("Digite a escala de saída: Celsius, Fahrenheit ou Kelvin (ou C, F ou K): ").upper()

# Escala de entrada Celsius
if escala_entrada == "CELSIUS" or  escala_entrada == "C":
    if escala_saida == "FAHRENHEIT" or escala_saida == "F":
        temperatura_convertida = (temperatura_entrada * (9/5)) + 32
        print(f"{temperatura_entrada} Cº = {temperatura_convertida:.2f} Fº")
    elif escala_saida == "KELVIN" or escala_saida == "K": 
        temperatura_convertida = temperatura_entrada + 273.15
        print(f"{temperatura_entrada} Cº = {temperatura_convertida:.2f} Kº")
    else:
        print(temperatura_entrada,"Cº")
# Escala de entrada Fahrenheit
elif escala_entrada == "FAHRENHEIT" or escala_entrada == "F":
    if escala_saida == "CELSIUS" or escala_saida == "C":
        temperatura_convertida = (temperatura_entrada - 32) * (5/9)
        print(f"{temperatura_entrada} Fº = {temperatura_convertida:.2f} Cº")
    elif escala_saida == "KELVIN" or escala_saida == "K": 
        temperatura_convertida = (temperatura_entrada - 32) * (5/9) + 273.15
        print(f"{temperatura_entrada} Fº = {temperatura_convertida:.2f} Kº")
    else:
        print(temperatura_entrada,"Fº")
#Escala de entrada Kelvin
else:
    if escala_saida == "FAHRENHEIT" or escala_saida == "F":
        temperatura_convertida = (temperatura_entrada * (9/5)) - 459.67
        print(f"{temperatura_entrada} Kº = {temperatura_convertida:.2f} Fº")
    elif escala_saida == "CELSIUS" or escala_saida == "C": 
        temperatura_convertida = temperatura_entrada - 273.15
        print(f"{temperatura_entrada} Kº = {temperatura_convertida:.2f} Cº")
    else:
        print(temperatura_entrada,"Kº")
        