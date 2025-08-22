import locale

locale.setlocale(locale.LC_ALL, "")

produto = {
    "Nome": "Cadeira infatil",
    "Preço Unitário": 12.40,
    "Quantidade": 3
}

soma_total = produto.get("Preço Unitário") * produto.get("Quantidade")

print("TOTAL DA COMPRA:")
print(f"{"Nome"}  -  {"Preço Unitário"}  -  {"Quantidade"} \n\n".upper())
print(f"{produto.get("Nome")}  -  R$ {produto.get("Preço Unitário"):.2f}  -  {produto.get("Quantidade")} \n\n".upper())
print("--------------------------")
print(f"Valor: {soma_total:.2f}".upper())