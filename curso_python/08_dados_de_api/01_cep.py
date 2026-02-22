# %%

import requests # para realizar requisições na web
import json # para tratar json de listas/dicionários para arquivos json
from tqdm import tqdm

import pandas as pd

# %%
ceps = [
    '01014-000',
    '01033-000',
    '01044-000',
    '01310-928',
    '01503-000',
    '03011-001',
    '03014-000',
    '04010-000',
    '04308-000',
    '04309-010',
    '04551-000',
]


url = 'https://viacep.com.br/ws/{cep}/json/'
dados = []

for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

dados

# %%

dataset = pd.DataFrame(dados)
dataset.to_csv('ceps.csv', sep=';')


# %%

print(dados)

with open('ceps.json', 'w', encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4 )