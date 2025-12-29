# Exercício 6 — Tabuada
# Peça ao usuário um número inteiro e mostre a tabuada completa desse número (de 1 a 10) usando laço de repetição.

# %%

numero = int(input('Digite um número: '))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f'{numero} x {multiplicador} = {resultado}')
