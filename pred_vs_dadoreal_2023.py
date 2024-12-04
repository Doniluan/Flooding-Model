import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_pred_vs_real_2023():
    # Dados
    estados = ["RS", "PR", "SP", "RJ", "MG", "SC"]
    categorias = ["Sem Risco", "Risco Baixo", "Risco Moderado", "Risco Elevado", "Risco Crítico"]

    dados_reais = {
        "RS": [2134, 1349, 247, 26, 157],
        "PR": [2569, 810, 120, 23, 1],
        "SP": [1911, 1101, 183, 11, 10],
        "RJ": [1907, 929, 244, 14, 25],
        "MG": [2479, 920, 126, 46, 7],
        "SC": [2059, 1470, 404, 70, 8]
    }

    previsoes = {
        "RS": [1906, 1019, 351, 30, 151],
        "PR": [2375, 591, 205, 61, 5],
        "SP": [1880, 690, 273, 21, 10],
        "RJ": [1866, 555, 445, 20, 25],
        "MG": [2266, 605, 188, 53, 10],
        "SC": [1867, 1192, 210, 16, 4]
    }

    # Título
    st.subheader("Comparação Previsões vs Dados Reais - 2023")

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
    st.title("Dashboard de Comparação - Previsões vs Dados Reais (2023)")
    plot_pred_vs_real_2023()
