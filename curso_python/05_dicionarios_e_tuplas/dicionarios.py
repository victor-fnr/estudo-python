# %%

lista = [7, 99, "victor", ["a", "b", "c"], True]

lista[2]

# %%

# pares de chave/valor

dados_victor = {
    "sobrenome":"Ribeiro",
    "nome":"Victor", 
    "filhos":False,
    "formacao":["ADS", "AD"],
    "cargos":[
        {"nome": "ds jr.", "empresa": "Serena"},
        {"nome": "ds pl.", "empresa": "Bradesco" },
        {"nome": "ds sr.", "empresa": "Microsoft"},
        {"nome": "ds espec.", "empresa": "Google"},
    ]
}

# %%
print(dados_victor)
print(dados_victor["formacao"][-1])
print(dados_victor["cargos"][-1]["empresa"])

# %%
dados_victor["estado civil"] = "solteiro"

# %%

print("Chaves:", dados_victor.keys())
print("Valores:", dados_victor.values())
print("Items:", dados_victor.items())

# %%

for i in [10,20,45,28,"Victor"]:
    print(i)

# %%

for i in dados_victor:
    print(i, "->", dados_victor[i])

# %%

for chave, valor in dados_victor.items():
    print(chave, "->", valor)

# %%

dados_victor["estado civil"] = "casado"
dados_victor["fodase"] = None
# %%
dados_victor