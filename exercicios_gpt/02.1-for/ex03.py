# %%
# Exercício 3 — Soma de valores
# Peça ao usuário 5 números inteiros e utilize um for para calcular a soma total.

soma = 0
for i in range(5):
    i = int(input('Digite um número: '))
    soma += i
    
print(soma)

