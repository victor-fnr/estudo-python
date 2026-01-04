# %%

def par_impar(numero:int)->int:
    if numero % 2 == 0:
        print(f'{numero} é par!')
    else:
        print(f'{numero} é Ímpar!')

numero = input('Entre com um número: ')
numero = int(numero)

par_impar(numero)

# %%

def par_impar(numero:int)->int:
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'

numero = input('Entre com um número: ')
numero = int(numero)

resultado = par_impar(numero)

print(f'O valor {numero} é {resultado}!')