import streamlit as st
import joblib
import numpy as np

# Função para carregar o modelo de acordo com o estado selecionado
def carregar_modelo(estado):
    nome_arquivo = f"{estado}_Flooding_Model.joblib"
    try:
        with open(nome_arquivo, "rb") as file:
            modelo = joblib.load(file)
        return modelo
    except FileNotFoundError:
        st.error(f"O modelo para o estado {estado} não foi encontrado.")
        st.stop()

# Função para transformar os dados
def transformar_dados(dados):
    # Normalizar os valores numéricos
    precipitacao_normalizada = dados["precipitacao"] 
    cobertura_normalizada = dados["cobertura_vegetal"] 

    # Mapeamento da Altitude (por exemplo, mapeando Baixa, Média, Alta)
    altitude_map = {'Baixa': 1, 'Média': 2, 'Alta': 3}
    altitude_codificada = altitude_map.get(dados["altitude"], 2)  # Padrão "Média" se não encontrado

    # Problemas de drenagem codificados (0: Não, 1: Sim)
    drenagem_codificada = 1 if dados["problemas_drenagem"] == "sim" else 0

    # Combinar as variáveis para formar a entrada para o modelo
    entrada_transformada = [
        precipitacao_normalizada,
        cobertura_normalizada,
        altitude_codificada,
        drenagem_codificada
    ]
    
    # Retorna a entrada transformada em formato de array para o modelo
    return np.array([entrada_transformada])

# Interface do Streamlit
st.title("Sistema de Previsão de Risco de Enchentes")
st.markdown(
    """
    Este aplicativo utiliza modelos de Machine Learning para prever o risco de enchentes com base nos dados fornecidos.
    """
)

# Seleção do estado
estado = st.selectbox(
    "Selecione o Estado",
    options=["SP", "RJ", "MG", "SC", "RS", "PR"],
    help="Escolha o estado para realizar a previsão."
)

# Carregar o modelo com base no estado selecionado
rf_salva = carregar_modelo(estado)

# Formulário de entrada de dados
st.header("Informe os Dados")
precipitacao = st.number_input("Precipitação (mm)", min_value=0.0, step=0.1)
cobertura_vegetal = st.number_input("Cobertura Vegetal (%)", min_value=0.0, max_value=100.0, step=0.1)
altitude = st.selectbox("Altitude", options=["Baixa", "Média", "Alta"])
problemas_drenagem = st.selectbox("Problemas de Drenagem", options=["sim", "não"])

# Mapeamento de categorias de risco de alagamento
risco_map = {
    0: "Sem Risco",
    1: "Risco Baixo",
    2: "Risco Moderado",
    3: "Risco Elevado",
    4: "Risco Crítico"
}

# Quando o botão for clicado, realizar a previsão
if st.button("Prever Risco"):
    # Preparar os dados
    dados = {
        "precipitacao": precipitacao,
        "cobertura_vegetal": cobertura_vegetal,
        "altitude": altitude,
        "problemas_drenagem": problemas_drenagem,
    }
    try:
        # Transformar os dados antes de passar para a previsão
        entrada_transformada = transformar_dados(dados)

        # Realizar a previsão
        previsao = rf_salva.predict(entrada_transformada)

        # Exibir o risco de alagamento como uma descrição completa
        st.success(f"O risco previsto de enchente é: {risco_map.get(previsao[0], 'Desconhecido')}")
    except Exception as e:
        st.error(f"Erro ao realizar a previsão: {e}")
