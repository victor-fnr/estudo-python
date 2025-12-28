# Exercício 4 — Classificação de idade
# Solicite a idade de uma pessoa e classifique-a em:
# criança (0 a 12),
# adolescente (13 a 17),
# adulto (18 a 59),
# idoso (60 ou mais).

# %%

idade = int(input('Digite uma idade: '))

if idade < 0:
    print('Idade inválida.')
elif idade <= 12:
    print('Criança')
elif idade <= 17:
    print('Adolescente')
elif idade <= 59:
    print('Adulto(a)')
else:
    print('Idoso(a)')
