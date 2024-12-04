import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def plot_validacao_cruzada():

    st.subheader("Análise das médias das Validações Cruzadas")
    
    # Dados das validações cruzadas
    val_scores = {
        "SP": np.array([0.99821747, 0.99286988, 0.99821747, 0.99286988, 0.98752228]),
        "RJ": np.array([0.90163934, 1.        , 0.98907104, 0.70673953, 0.92531876]),
        "MG": np.array([0.80819672, 1.        , 0.79180328, 0.88196721, 0.62131148]),
        "SC": np.array([0.99701937, 0.60506706, 0.78241431, 0.8733234 , 0.94485842]),
        "RS": np.array([1.        , 0.99850969, 0.8271237 , 1.        , 1.        ]),
        "PR": np.array([0.96945338, 0.95176849, 0.99356913, 0.99839228, 0.99517685]),
    }

    # Calcular as médias
    means = {state: scores.mean() for state, scores in val_scores.items()}

    # Criar o gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    states = list(means.keys())
    avg_scores = list(means.values())

    # Barras das médias
    ax.bar(states, avg_scores, color="skyblue", edgecolor="black", alpha=0.8)

    # Personalizar o gráfico
    ax.set_title("Média das Validações Cruzadas por Estado", fontsize=14, fontweight='bold')
    ax.set_ylabel("Média da Acurácia", fontsize=12)
    ax.set_xlabel("Estado", fontsize=12)
    ax.set_ylim(0, 1.1)  # Para visualizar 1.0 claramente
    ax.axhline(y=1.0, color='gray', linestyle='--', linewidth=1, label='Perfeição (1.0)')
    ax.legend(loc="lower right")

    # Adicionar valores no topo das barras
    for i, v in enumerate(avg_scores):
        ax.text(i, v + 0.02, f"{v:.3f}", ha='center', fontsize=10, fontweight='bold')

    st.pyplot(fig)
