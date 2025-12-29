# Exercício 8 — Análise de lista
# Crie uma lista com números inteiros.
# Utilize um laço para determinar:
# o maior valor,
# o menor valor,
# a quantidade de elementos.

# %%

lista = []

while True:
    valor = input('Digite um número (ENTER para finalizar): ')
    if valor == '':
        break
    valor = int(valor)
    lista.append(valor)


maior = lista[0]
menor = lista[0]
quantidade = 0

for numero in lista:
    quantidade += 1

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print(f'Quantidade: {quantidade}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')
