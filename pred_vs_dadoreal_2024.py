import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Função para plotar os gráficos
def plot_pred_vs_real_2024():
    # Dados
    estados = ['RS', 'PR', 'SP', 'RJ', 'MG', 'SC']
    categorias = ['Sem Risco', 'Risco Baixo', 'Risco Moderado', 'Risco Elevado', 'Risco Crítico']
    dados_reais = {
        'RS': [1906, 1010, 247, 26, 157],
        'PR': [2375, 591, 120, 23, 1],
        'SP': [1911, 690, 183, 11, 10],
        'RJ': [1907, 555, 244, 14, 25],
        'MG': [2266, 605, 126, 46, 7],
        'SC': [1866, 1192, 300, 13, 73],
    }
    previsoes = {
        'RS': [1906, 1019, 247, 26, 157],
        'PR': [2375, 592, 119, 23, 1],
        'SP': [1911, 690, 182, 12, 10],
        'RJ': [1907, 555, 244, 14, 25],
        'MG': [2266, 606, 125, 45, 8],
        'SC': [1866, 1103, 300, 16, 73],
    }

    # Título
    st.subheader("Comparação Previsões vs Dados Reais - 2024")

       # Gráficos para RS e PR
    st.write("### Comparação para RS e PR")
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    for i, estado in enumerate(["RS", "PR"]):
        x = np.arange(len(categorias))
        largura = 0.35

        ax[i].bar(x - largura / 2, dados_reais[estado], largura, label="Dados Reais", color="royalblue")
        ax[i].bar(x + largura / 2, previsoes[estado], largura, label="Previsões", color="darkorange")
        ax[i].set_title(f"Comparação - {estado}")
        ax[i].set_xticks(x)
        ax[i].set_xticklabels(categorias, rotation=15)
        ax[i].set_ylabel("Quantidade")
        ax[i].legend()

    st.pyplot(fig)

    # Gráficos para SP e RJ
    st.write("### Comparação para SP e RJ")
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    for i, estado in enumerate(["SP", "RJ"]):
        x = np.arange(len(categorias))
        largura = 0.35

        ax[i].bar(x - largura / 2, dados_reais[estado], largura, label="Dados Reais", color="royalblue")
        ax[i].bar(x + largura / 2, previsoes[estado], largura, label="Previsões", color="darkorange")
        ax[i].set_title(f"Comparação - {estado}")
        ax[i].set_xticks(x)
        ax[i].set_xticklabels(categorias, rotation=15)
        ax[i].set_ylabel("Quantidade")
        ax[i].legend()

    st.pyplot(fig)

    # Gráficos para MG e SC
    st.write("### Comparação para MG e SC")
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    for i, estado in enumerate(["MG", "SC"]):
        x = np.arange(len(categorias))
        largura = 0.35

        ax[i].bar(x - largura / 2, dados_reais[estado], largura, label="Dados Reais", color="royalblue")
        ax[i].bar(x + largura / 2, previsoes[estado], largura, label="Previsões", color="darkorange")
        ax[i].set_title(f"Comparação - {estado}")
        ax[i].set_xticks(x)
        ax[i].set_xticklabels(categorias, rotation=15)
        ax[i].set_ylabel("Quantidade")
        ax[i].legend()

    st.pyplot(fig)

# Executa a função
if __name__ == "__main__":
    st.title("Dashboard de Comparação - Previsões vs Dados Reais")
    plot_pred_vs_real_2024()
