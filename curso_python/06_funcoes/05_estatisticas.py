# %%

def soma(a:float, b:float)->float:
    return a + b

def media(a:float, b:float)->float:
    return soma(a, b) / 2

a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))

print(f'Média {media(a, b)}')

# %%

def soma(a:float, b:float, *args)->float:
    valores = [a, b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args)->float:
    return soma(a, b, *args) / (len(args)+2)

a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

print(f'Média {media(a, b, c)}')

# %%

def soma(valores:list)->float:
    return sum(valores)

def media(valores:list)->float:
    return soma(valores) / len(valores)

valores = []

while True:
    numero = input('Entre com um valor (ENTER para finalizar): ')

    if numero == '':
        break

    numero = int(numero)
    valores.append(numero)

if len(valores) > 0:
    print(f'Média: {media(valores)}')
else:
    print('Nenhum valor informado.')