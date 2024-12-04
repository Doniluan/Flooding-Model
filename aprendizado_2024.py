import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
import streamlit as st
from variaveis2024 import get_variaveis_SP2024, get_variaveis_RJ2024, get_variaveis_MG2024, get_variaveis_SC2024, get_variaveis_RS2024, get_variaveis_PR2024
from modelos import carregar_modeloSP, carregar_modeloRJ, carregar_modeloMG, carregar_modeloSC, carregar_modeloRS, carregar_modeloPR

def plot_aprendizado_2024():

    st.subheader("Curva de Aprendizado 2024")

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
        
        # Plotando a curva de aprendizado
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(train_sizes, train_mean, label="Treinamento (Média)", color="blue", marker='o')
        ax.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.2, color="blue")
        
        ax.plot(train_sizes, test_mean, label="Validação (Média)", color="orange", marker='s')
        ax.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, alpha=0.2, color="orange")
        
        # Configurações do gráfico
        ax.set_title(f"Curva de Aprendizado - {estado}", fontsize=14)
        ax.set_xlabel("Quantidade de Dados de Treinamento", fontsize=12)
        ax.set_ylabel("Acurácia", fontsize=12)
        ax.legend(loc="best")
        ax.grid()
        plt.tight_layout()
        
        return fig  # Agora retornamos a figura gerada

    # Gerando as variáveis
    X_SP2, y_SP2 = get_variaveis_SP2024()
    X_RJ2, y_RJ2 = get_variaveis_RJ2024()
    x_MG2, y_MG2 = get_variaveis_MG2024()
    x_SC2, y_SC2 = get_variaveis_SC2024()
    X_RS2, y_RS2 = get_variaveis_RS2024()
    X_PR2, y_PR2 = get_variaveis_PR2024()

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
    dados_X = [X_SP2, X_RJ2, x_MG2, x_SC2, X_RS2, X_PR2]
    dados_y = [y_SP2, y_RJ2, y_MG2, y_SC2, y_RS2, y_PR2]  # Alvos correspondentes

    for estado, modelo, X, y in zip(estados, modelos, dados_X, dados_y):
        print(f"Gerando curva de aprendizado para {estado}...")
        fig = plot_learning_curve(modelo, X, y, estado)
        st.pyplot(fig)  # Exibe a figura no Streamlit
