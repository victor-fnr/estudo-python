# %%
# Exercício 7 — Verificação de existência

# Verifique se uma determinada chave existe em um dicionário antes de tentar acessá-la.

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

while True:
    chave = input('Digite a chave: ')
    if chave == '':
        break

    if chave in dados_victor.keys():
         print(f'Chave: \'{chave}\' encontrada | Valor: {dados_victor[chave]}')
         continue
    else:
        print(f'Chave: \'{chave}\' não encontrada')
        continue
