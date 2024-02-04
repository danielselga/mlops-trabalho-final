import requests
import pandas as pd
import json



if __name__ == "__main__":


    # Filtra alguns para testes:
    
    data_json = {
    "Transaction ID": 1,
    "Date": "19/10/2023",
    "Time": "05:31",
    "Card Type": "MasterCard",
    "Entry Mode": "Tap",
    "Amount": 391.56,
    "Transaction Type": "POS",
    "Merchant Group": "Clothing",
    "Transaction Country": "Italy",
    "Shipping Address": "61 Redwood St",
    "Billing Address": "726 Maple St",
    "Gender": "Female",
    "Age": 55,
    "Issuing Bank": "XYZ Bank",
    }

    # Prepara chamada
    url = "http://192.168.0.188:8081/modelo01"
    headers = {'Content-Type': 'application/json'}
    # Convertendo o dicionário Python para uma string JSON
    data_json_str = json.dumps(data_json)

    # Chama a API
    response = requests.post(url, headers=headers, data=data_json_str)
                             
    print("Resposta da API:")
    print(response.text.encode('utf8').decode())
    pass

