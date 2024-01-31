# Coloque aqui o código do teu cliente em Python

import requests
import pandas as pd
import json


if __name__ == "__main__":
    # Carrega os dados
    mydf = pd.read_csv('../../datasets/BaseUnknown03.csv')

    # Filtra alguns para testes:
    filtrados = mydf.sample(4)

    # Prepara chamada
    url = "http://localhost:8080/modelo01"
    headers = {'Content-Type': 'application/json'}
    conteudo = filtrados.to_json()

    #Chama API
    response = requests.request("POST", url, headers=headers, data=conteudo)
    print("Resposta da API:")
    print(response.text.encode('utf8').decode())


    # Carrega os dados
    mydf = pd.read_csv('../../datasets/BaseUnknown03.csv')

    # Filtra alguns para testes:
    filtrados = mydf.sample(4)

    # Prepara chamada
    url = "http://localhost:8080/modelo02"
    headers = {'Content-Type': 'application/json'}
    conteudo = filtrados.to_json()

    #Chama API
    response2 = requests.request("POST", url, headers=headers, data=conteudo)
    print("Resposta da API:")
    print(response2.text.encode('utf8').decode())



    response_1 = json.loads(response.text)
    response_2 = json.loads(response2.text)

    # Criar dataframes com os dados
    df1 = pd.DataFrame(response_1)
    df2 = pd.DataFrame(response_2)

    # Concatenar os dataframes ao longo das colunas (axis=1)
    result_df = pd.concat([df1, df2], axis=1)

    # Salvar o dataframe em um arquivo CSV
    result_df.to_csv('resultado.csv', index=False)