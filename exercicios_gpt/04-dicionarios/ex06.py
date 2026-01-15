# %%
# Exercício 6 — Contagem com dicionário
# Leia uma frase do usuário e utilize um dicionário para contar quantas vezes cada palavra aparece.

frase = input('Frase: ')

contagem = {}


for palavra in frase.split():
    
    if palavra not in contagem:
        contagem[palavra] = 1
    else:
        contagem[palavra] += 1

for chave, valor in contagem.items():
    print(f'Palavra: {chave} | Quantidade: {valor}')
        

    