# Exercício 9 — Sistema de imposto
# Crie um programa que leia o salário de um funcionário e calcule a alíquota de imposto conforme faixas salariais definidas por você.
# O programa deve exibir:
# salário bruto,
# percentual aplicado,
# valor do imposto.

# %%

# Até R$ 2.000,00
# → Isento (0%)
# De R$ 2.000,01 até R$ 3.000,00
# → 8% de imposto
# De R$ 3.000,01 até R$ 5.000,00
# → 15% de imposto
# Acima de R$ 5.000,00
# → 22% de imposto

salario = float(input('Digite o salário bruto do funcionário: '))

if salario > 0:

    if 0 < salario <= 2000:
        aliquota = 0
        

    elif 2000 < salario <= 3000:
        aliquota = 0.08

    elif 3000 < salario <= 5000:
        aliquota = 0.15

    else:
        aliquota = 0.22

else:
    print('Salário inválido')

imposto = aliquota * salario
liquido = salario - imposto

print(f'O salário bruto do fúncionario é: R${salario:.2f}')
print(f'O percentual aplicado é de {aliquota * 100:.0f}%')    
print(f'O valor do imposto é: R${imposto:.2f}')
print(f'O salário líquido é: R${liquido:.2f}')