import pandas as pd
import json
import numpy as np
import random
from flask import Flask, jsonify, request
# Importando as bibliotecas necessárias
# Libs para análise exploratória
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.utils.class_weight import compute_class_weight
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from tensorflow.keras.models import Sequential, load_model, model_from_json
from tensorflow.keras.layers import Dense, Conv1D, Flatten, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from joblib import load



app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def call_home(request = request):
    print(request.values)
    return "SERVER do modelo 1 está funcioando!"

@app.route("/modelo01", methods=['POST'])
def call_modelo01(request = request):

    print(request.values)
 
    # Convertendo o JSON em um DataFrame do pandas

    dados = pd.DataFrame([request.json])

    # Supondo que 'preprocessor' já esteja definido e carregado corretamente
    input_processed = preprocessor.transform(dados)
    input_processed_d = input_processed.toarray()
    input_processed_reshaped = input_processed_d.reshape(input_processed_d.shape[0], input_processed_d.shape[1], 1)
    
    # Certifique-se de que 'model' está definido e carregado corretamente
    previsoes = model.predict(input_processed_reshaped)
    print(previsoes)
    
    # Retornando o primeiro valor da previsão como JSON
    return jsonify({"previsão": previsoes[0].item()})  # Use .item() para converter o valor numpy para Python nativo


preprocessor = load('preprocessor.joblib')

# Carregando o modelo no formato DHF5
model = load_model('./modeloServer2.h5')

model.load_weights('./modeloServer2weights.h5')
# Salvando o modelo no formado HDF5


if __name__ == '__main__':
    app.run(port=8081, host = '0.0.0.0')
    #app.run(port=8080)
    # pass


