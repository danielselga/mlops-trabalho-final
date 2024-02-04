import joblib
import pandas as pd
import json
import numpy as np
import random
from flask import Flask, jsonify, request
from joblib import load

modelo = load('modelo_regressao_linear.joblib')


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def call_home(request = request):
    print(request.values)
    return "SERVER do modelo 2 está funcioando!"


@app.route("/modelo01", methods=['POST'])
def call_modelo01():
    try:  
        dados = pd.DataFrame([request.json])
        print(dados)
        dados = dados[['Amount', 'Age']]  # Substitua com valores novos
        previsao = modelo.predict(dados)
        print(previsao)
        ret = jsonify({"numero_previsto": previsao[0].item()})
        return ret
    except:
        # Acessando o JSON da requisição
        numero_aleatorio = random.random()
        print(numero_aleatorio)
        
        # Criando a resposta como JSON
        ret = jsonify({"numero_aleatorio": numero_aleatorio})
        return ret

if __name__ == '__main__':
    app.run(port=8082, host='0.0.0.0')
