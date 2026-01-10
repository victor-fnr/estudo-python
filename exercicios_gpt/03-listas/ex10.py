# %%
# Exercício 10 — Análise de dados
# Crie um programa que utilize uma lista para armazenar dados (ex.: notas, salários ou idades) e:
# calcule média,
# identifique valores acima e abaixo da média,
# gere um resumo final.

notas = []

while True:
    nota = input('Nota: ')
    if not nota:
        break

    try:
        nota = float(nota)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print('[ERRO] Nota deve estar entre 0 e 10.')
    except ValueError:
        print('[ERRO] Digite uma nota válida.')

if not notas:
    print('[ERRO] Nenhuma nota adicionada.')
else:
    media = sum(notas) / len(notas)

    acima = []
    abaixo = []

    for nota in notas:
        if nota > media:
            acima.append(nota)
        elif nota < media:
            abaixo.append(nota)

    print(f'Média: {media:.2f}')
    print(f'Notas acima da média: {acima}')
    print(f'Notas abaixo da média: {abaixo}')
