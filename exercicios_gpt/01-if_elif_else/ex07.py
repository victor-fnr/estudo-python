# Exercício 7 — Ano bissexto
# Leia um ano e determine se ele é bissexto, considerando as regras oficiais:
# divisível por 4,
# mas não por 100, exceto se também for divisível por 400.

# %%

ano = int(input("Digite um ano: "))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print("Ano bissexto")
else:
    print("Ano não bissexto")
