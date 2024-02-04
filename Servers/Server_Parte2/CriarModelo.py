# Libs para análise exploratória
import numpy as np
import pandas as pd
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
from joblib import dump

# Supondo que 'preprocessor' é o seu ColumnTransformer ajustado


dados = pd.read_csv('../serving/dataset.csv', delimiter=';')

print(dados.head(3))

# Separação das variáveis independentes e dependentes
X = dados.drop('Fraudulent', axis=1)
y = dados['Fraudulent'].map({'Yes': 1, 'No': 0})  # Convertendo a variável alvo para formato numérico

# Divisão dos dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Seleção de colunas numéricas e categóricas
colunas_numericas = X_train.select_dtypes(include=['int64', 'float64']).columns
colunas_categoricas = X_train.select_dtypes(include=['object']).columns

# Normalização para colunas numéricas
transformador_numerico = Pipeline(steps=[
    ('scaler', StandardScaler())
])

# Codificação one-hot para colunas categóricas
transformador_categorico = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combinando transformadores em um único transformador de coluna
preprocessor = ColumnTransformer(
    transformers=[
        ('num', transformador_numerico, colunas_numericas),
        ('cat', transformador_categorico, colunas_categoricas)
    ])


# 5. Aplicando o pré-processamento aos dados de treinamento e teste
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# Convertendo as matrizes esparsas em arrays densos
X_train_dense = X_train_processed.toarray()
X_test_dense = X_test_processed.toarray()

# Redimensionamento dos dados para o formato necessário para uma CNN
X_train_reshaped = X_train_dense.reshape(X_train_dense.shape[0], X_train_dense.shape[1], 1)
X_test_reshaped = X_test_dense.reshape(X_test_dense.shape[0], X_test_dense.shape[1], 1)

X_train_final, X_val, y_train_final, y_val = train_test_split(X_train_reshaped, y_train, test_size=0.2, random_state=42)

model = Sequential()
model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(X_train_reshaped.shape[1], 1)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(50, activation='relu'))
model.add(Dense(1, activation='sigmoid'))  # Sigmoid para classificação binária

model.compile(optimizer=Adam(learning_rate=0.0001), loss='binary_crossentropy', metrics=['accuracy'])


model.compile(optimizer=Adam(learning_rate=0.0001), loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(X_train_final, y_train_final, epochs=5, batch_size=32, validation_data=(X_val, y_val), verbose=1)

# Fazendo previsões no conjunto de teste
predictions = model.predict(X_test_reshaped)
predicted_classes = np.round(predictions).flatten()  # Arredondando as previsões para obter a classe

# Salvando o modelo no formado HDF5
model.save('./modeloServer2.h5')
# Arquitetura das camadas em JSON e pesos treinados em HDF5
model.save_weights('./modeloServer2weights.h5')

print("Modelo gravado com sucesso")

dump(preprocessor, 'preprocessor.joblib')