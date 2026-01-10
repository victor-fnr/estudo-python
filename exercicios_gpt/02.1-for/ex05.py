# %%
# Exercício 5 — Tabuada com for
# Peça ao usuário um número inteiro e utilize um for para exibir a tabuada completa desse número (1 a 10).

tabuada = int(input('Digite a tabuada a ser exibida: '))
for i in range(1, 11):
    resultado = tabuada * i
    print(f'{tabuada} x {i} = {resultado}')


