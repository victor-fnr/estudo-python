# Exercício 7 — Média de notas
# Solicite várias notas ao usuário até que ele informe um valor de parada (por exemplo, -1).
# Calcule e exiba a média das notas válidas informadas.

# %%
contador = 0
soma = 0

while True:
    nota = float(input('Digite uma nota: '))
    if nota == -1:
        break
    soma += nota
    contador += 1

if contador > 0:
    media = soma / contador
    print(f'Média das notas: {media}')
else:
    print('Nenhuma nota válida foi informada.')