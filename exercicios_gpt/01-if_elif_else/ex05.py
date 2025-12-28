# Exercício 5 — Nota escolar
# Leia uma nota de 0 a 10 e informe:
# Reprovado (nota menor que 5),
# Recuperação (nota entre 5 e 6.9),
# Aprovado (nota 7 ou maior).
# Inclua uma verificação para notas inválidas.

# %%

nota = float(input('Digite a nota: '))

if nota < 0 or nota > 10:
    print('Nota inválida')
elif 0 <= nota < 5:
    print('Reprovado')
elif 5 <= nota < 7:
    print('Recuperação')
else:
    print('Aprovado')
