# %%
# Exercício 6 — Percorrendo listas
# Crie uma lista com valores numéricos e utilize um for para:
# exibir cada elemento,
# calcular o maior valor da lista.

lista = []

while True:
    numero = input('Digite um número (ENTER para sair): ')
    if numero == '':
        break
    numero = int(numero)
    lista.append(numero)

maior = lista[0]

for numero in lista:
    print(numero)

    if numero > maior:
        maior = numero

print(f'Maior número: {maior}')

