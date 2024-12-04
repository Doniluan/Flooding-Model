import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def plot_risco_2023():

    st.subheader("Distribuição de Risco 2023")

    # Dados de 2023
    data_2023 = {
        "SP": [1880, 1101, 273, 21, 10],
        "RJ": [1866, 929, 444, 19, 27],
        "MG": [2479, 928, 236, 0, 7],
        "SC": [2059, 1647, 289, 15, 5],
        "RS": [2134, 1349, 505, 4, 23],
        "PR": [2569, 848, 228, 5, 0]
    }

    # Convertendo os dados em um DataFrame
    df_2023 = pd.DataFrame(data_2023, index=["Sem Risco", "Risco Baixo", "Risco Moderado", "Risco Elevado", "Risco Crítico"])

    # Exibindo os gráficos um por um para cada estado
    estados = df_2023.columns.tolist()

    for estado in estados:
        st.subheader(f"Distribuição de Risco em {estado} (2023)")

        # Criando o gráfico
        fig, ax = plt.subplots(figsize=(8, 6))
        bars = df_2023[estado].plot(kind='bar', ax=ax, color=plt.cm.tab10(estados.index(estado)))

        ax.set_xlabel("Categorias de Risco")
        ax.set_ylabel("Número de Ocorrências")
        ax.set_title(f"Distribuição de Risco em {estado} (2023)")
        ax.tick_params(axis='x', rotation=45)

        # Adicionando rótulos nas barras
        for p in bars.patches:
            ax.annotate(f'{p.get_height()}', 
                        (p.get_x() + p.get_width() / 2, p.get_height()), 
                        ha='center', va='center', fontsize=9, 
                        xytext=(0, 5), textcoords='offset points')

        # Exibindo o gráfico no Streamlit
        st.pyplot(fig)