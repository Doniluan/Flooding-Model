import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
import streamlit as st
from variaveis2023 import get_variaveis_SP2023, get_variaveis_RJ2023, get_variaveis_MG2023, get_variaveis_SC2023, get_variaveis_RS2023, get_variaveis_PR2023
from modelos import carregar_modeloSP, carregar_modeloRJ, carregar_modeloMG, carregar_modeloSC, carregar_modeloRS, carregar_modeloPR

def plot_aprendizado_2023():

    st.subheader("Curva de Aprendizado 2023")

    # Função para plotar a curva de aprendizado
    def plot_learning_curve(model, X, y, estado):
        train_sizes, train_scores, test_scores = learning_curve(
            model, X, y, cv=5, scoring='accuracy', train_sizes=np.linspace(0.1, 1.0, 10), n_jobs=-1
        )
        
        # Média e desvio padrão dos scores
        train_mean = np.mean(train_scores, axis=1)
        train_std = np.std(train_scores, axis=1)
        test_mean = np.mean(test_scores, axis=1)
        test_std = np.std(test_scores, axis=1)
        
        # Criando a figura
        plt.figure(figsize=(8, 6))
        plt.plot(train_sizes, train_mean, label="Treinamento (Média)", color="blue", marker='o')
        plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.2, color="blue")
        
        plt.plot(train_sizes, test_mean, label="Validação (Média)", color="orange", marker='s')
        plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, alpha=0.2, color="orange")
        
        # Configurações do gráfico
        plt.title(f"Curva de Aprendizado - {estado}", fontsize=14)
        plt.xlabel("Quantidade de Dados de Treinamento", fontsize=12)
        plt.ylabel("Acurácia", fontsize=12)
        plt.legend(loc="best")
        plt.grid()
        plt.tight_layout()

        # Retorna a figura
        return plt

    # Gerando as variáveis
    X_SP, y_SP = get_variaveis_SP2023()
    X_RJ, y_RJ = get_variaveis_RJ2023()
    x_MG, y_MG = get_variaveis_MG2023()
    x_SC, y_SC = get_variaveis_SC2023()
    X_RS, y_RS = get_variaveis_RS2023()
    X_PR, y_PR = get_variaveis_PR2023()

    # Carregando os modelos 
    SP_rf_salva = carregar_modeloSP()
    RJ_rf_salva = carregar_modeloRJ()
    MG_rf_salva = carregar_modeloMG()
    SC_rf_salva = carregar_modeloSC()
    RS_rf_salva = carregar_modeloRS()
    PR_rf_salva = carregar_modeloPR()

    # Gerar curva de aprendizado para cada estado
    estados = ["SP", "RJ", "MG", "SC", "RS", "PR"]
    modelos = [SP_rf_salva, RJ_rf_salva, MG_rf_salva, SC_rf_salva, RS_rf_salva, PR_rf_salva]
    dados_X = [X_SP, X_RJ, x_MG, x_SC, X_RS, X_PR]
    dados_y = [y_SP, y_RJ, y_MG, y_SC, y_RS, y_PR]  # Alvos correspondentes

    for estado, modelo, X, y in zip(estados, modelos, dados_X, dados_y):
        print(f"Gerando curva de aprendizado para {estado}...")
        fig = plot_learning_curve(modelo, X, y, estado)
        st.pyplot(fig)

