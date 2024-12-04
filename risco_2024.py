import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def plot_risco_2024():

    st.subheader("Distribuição de Risco 2024")

    # Dados de 2024
    data_2024 = {
        "SP": [1911, 690, 183, 11, 10],
        "RJ": [1907, 555, 244, 14, 25],
        "MG": [2266, 614, 166, 0, 4],
        "SC": [1867, 1216, 259, 11, 2],
        "RS": [1906, 1019, 391, 8, 31],
        "PR": [2375, 619, 115, 1, 0]
    }

    # Convertendo os dados em um DataFrame
    df = pd.DataFrame(data_2024, index=["Sem Risco", "Risco Baixo", "Risco Moderado", "Risco Elevado", "Risco Crítico"])

    # Exibindo um gráfico por vez para cada estado
    estados = df.columns.tolist()
    
    for estado in estados:
        st.subheader(f"Distribuição de Risco em {estado} (2024)")

        # Criando o gráfico
        fig, ax = plt.subplots(figsize=(8, 6))
        bars = df[estado].plot(kind='bar', ax=ax, color=plt.cm.tab10(estados.index(estado)))

        ax.set_xlabel("Categorias de Risco")
        ax.set_ylabel("Número de Ocorrências")
        ax.set_title(f"Distribuição de Risco em {estado} (2024)")
        ax.tick_params(axis='x', rotation=45)

        # Adicionando rótulos nas barras
        for p in bars.patches:
            ax.annotate(f'{p.get_height()}', 
                        (p.get_x() + p.get_width() / 2, p.get_height()), 
                        ha='center', va='center', fontsize=9, 
                        xytext=(0, 5), textcoords='offset points')

        # Exibindo o gráfico no Streamlit
        st.pyplot(fig)