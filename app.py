import streamlit as st
from risco_enchente import prever_risco
from pred_vs_dadoreal_2024 import plot_pred_vs_real_2024
from pred_vs_dadoreal_2023 import plot_pred_vs_real_2023
from risco_2023 import plot_risco_2023
from risco_2024 import plot_risco_2024
from desempenho_p_estado import plot_desempenho_por_estado
from vali_cruzada import plot_validacao_cruzada
from aprendizado_2023 import plot_aprendizado_2023
from aprendizado_2024 import plot_aprendizado_2024
from erro_absoluto import erro_absoluto_model

# Título do aplicativo
st.title("Sistema de Previsão de Enchentes")
st.sidebar.title("Navegação")

# Menu de navegação
menu = st.sidebar.selectbox(
    "Escolha uma página",
    [
        "Prever Risco de Enchentes",
        "Comparação Previsões 2024",
        "Comparação Previsões 2023",
        "Distribuição de Risco 2023",
        "Distribuição de Risco 2024",
        "Desempenho do Modelo por Estado",
        "Validação Cruzada",
        "Curva de Aprendizado 2023",
        "Curva de Aprendizado 2024",
        "Erro Absoluto",
    ]
)

# Carregar a página correspondente com base na seleção do menu
if menu == "Prever Risco de Enchentes":
    prever_risco()

elif menu == "Comparação Previsões 2024":
    plot_pred_vs_real_2024()

elif menu == "Comparação Previsões 2023":
    plot_pred_vs_real_2023()

elif menu == "Distribuição de Risco 2023":
    plot_risco_2023()

elif menu == "Distribuição de Risco 2024":
    plot_risco_2024()

elif menu == "Desempenho do Modelo por Estado":
    plot_desempenho_por_estado()

elif menu == "Validação Cruzada":
    plot_validacao_cruzada()

elif menu == "Curva de Aprendizado 2023":
    plot_aprendizado_2023()

elif menu == "Curva de Aprendizado 2024":
    plot_aprendizado_2024()

elif menu == "Erro Absoluto":
    erro_absoluto_model()