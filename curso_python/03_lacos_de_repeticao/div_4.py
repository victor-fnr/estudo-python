# Quais números são divisiveis por 4
# Em um intervalo de [4-100]
# %%
divisor = 4

while divisor <= 100:
    resto = divisor % 4
    if resto == 0:
        print(divisor)
    divisor += 1 
