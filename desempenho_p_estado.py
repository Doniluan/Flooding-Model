import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def plot_desempenho_por_estado():

    
    # Dados de desempenho por estado
    estados = ["SP", "RJ", "MG", "SC", "RS", "PR"]
    accuracy = [1.00, 1.00, 1.00, 1.00, 1.00, 1.00]
    macro_avg_precision = [1.00, 1.00, 0.98, 1.00, 1.00, 0.80]
    macro_avg_recall = [1.00, 1.00, 0.87, 1.00, 1.00, 0.80]

    # Criar um gráfico separado para cada estado
    st.subheader("Comparação de Métricas de Desempenho por Estado")
    for i, estado in enumerate(estados):
        # Configurar os dados para o estado atual
        x = ["Accuracy", "Macro Avg Precision", "Macro Avg Recall"]
        y = [accuracy[i], macro_avg_precision[i], macro_avg_recall[i]]

        # Criar o gráfico
        fig, ax = plt.subplots(figsize=(6, 4))
        bars = ax.bar(x, y, color=["skyblue", "orange", "green"], width=0.6)

        # Adicionar rótulos e título
        ax.set_ylim(0, 1.1)
        ax.set_ylabel("Valor", fontsize=12)
        ax.set_title(f"Métricas de Desempenho - {estado}", fontsize=14)

        # Adicionar os valores no topo das barras
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.2f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # Deslocamento do texto
                        textcoords="offset points",
                        ha='center', va='bottom')

        # Exibir o gráfico no Streamlit
        st.pyplot(fig)

# Executa a função
if __name__ == "__main__":
    st.title("Dashboard de Desempenho por Estado")
    plot_desempenho_por_estado()
