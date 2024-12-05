import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def erro_absoluto_model():

    # Dados Reais
    dados_reais = {
        "RS": [4040, 2359, 494, 52, 314],
        "PR": [4944, 1401, 240, 46, 2],
        "SP": [3822, 1791, 366, 22, 20],
        "RJ": [3814, 1484, 488, 28, 50],
        "MG": [4745, 1525, 252, 92, 14],
        "SC": [3925, 2662, 704, 83, 81]
    }

    # Previsões
    previsoes = {
        "RS": [3812, 2038, 598, 56, 308],
        "PR": [4750, 1183, 324, 84, 6],
        "SP": [3791, 1380, 455, 33, 20],
        "RJ": [3773, 1110, 689, 34, 50],
        "MG": [4532, 1211, 313, 98, 18],
        "SC": [3733, 2295, 510, 32, 77]
    }

    # Categorias e Estados
    estados = ['RS', 'PR', 'SP', 'RJ', 'MG', 'SC']
    categorias = ['Sem Risco', 'Risco Baixo', 'Risco Moderado', 'Risco Elevado', 'Risco Crítico']

    # Calcular erros absolutos
    erros_absolutos = {estado: [abs(real - prev) for real, prev in zip(dados_reais[estado], previsoes[estado])]
                    for estado in estados}

    # Transformar os dados em um DataFrame para fácil manipulação e visualização
    df_erros = pd.DataFrame(erros_absolutos, index=categorias)

    # Configuração do Streamlit
    st.title("Análise de Erro Absoluto - Dados Totais")
    st.subheader("Erro Absoluto entre os Valores Reais e Previstos")

    # Mostrar a tabela de erros
    st.write("Tabela de Erros Absolutos:")
    st.dataframe(df_erros)

    # Plotar o heatmap de erro absoluto
    st.write("Heatmap de Erro Absoluto:")
    plt.figure(figsize=(10, 6))
    sns.heatmap(df_erros, annot=True, fmt="d", cmap="Reds", cbar=True, linewidths=0.5)
    plt.title("Erro Absoluto por Estado e Categoria")
    plt.xlabel("Estados")
    plt.ylabel("Categorias")
    st.pyplot(plt)
