import pandas as pd


def get_variaveis_SP2024():

    ## Criando DataFrames que serão Agrupados (SP)
    Braganca2 = pd.read_csv('Ambiente de teste-treinamento\SP2024_BP_tratado')
    BaseBraganca2 = Braganca2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Bertioga2 = pd.read_csv('Ambiente de teste-treinamento\SP2024_Bertioga_tratado')
    BaseBertioga2 = Bertioga2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Barueri2 = pd.read_csv('Ambiente de teste-treinamento\SP2024_Barueri_tratado')
    BaseBarueri2 = Barueri2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Iguape2 = pd.read_csv('Ambiente de teste-treinamento\SP2024_Iguape_tratado')
    BaseIguape2 = Iguape2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Taubate2 = pd.read_csv('Ambiente de teste-treinamento\SP2024_Taubate_tratado')
    BaseTaubate2 = Taubate2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    SP2 = pd.read_csv('Ambiente de teste-treinamento\SP2024_tratado')
    BaseInterlagos2 = SP2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    SLP2 = pd.read_csv('Ambiente de teste-treinamento\SP2024_SLP_tratado')
    BaseSLP2 = SLP2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Registro2 = pd.read_csv('Ambiente de teste-treinamento\SP2024_Registro_tratado')
    BaseRegistro2 = Registro2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Piracicaba2 = pd.read_csv('Ambiente de teste-treinamento\SP_Piracicaba_tratado')
    BasePira2 = Piracicaba2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]


    ## Agrupando todos DataFrames (SP)
    bases2 = [BaseBraganca2, BaseBertioga2, BaseBarueri2, BaseTaubate2, BasePira2, BaseRegistro2, BaseInterlagos2, BaseIguape2, BaseSLP2]
    nomes_estacoes2 = ['Braganca', 'Bertioga', 'Barueri', 'Taubate', 'Piracicaba', 'Registro', 'Interlagos', 'Iguape', 'São Luiz']

    for df, nome2 in zip(bases2, nomes_estacoes2):
        df['Estação (SP)'] = nome2

    BaseSP_Agrupado2 = pd.concat(bases2, ignore_index=True)
    colunas = ['Estação (SP)'] + [col for col in BaseSP_Agrupado2.columns if col != 'Estação (SP)']
    BaseSP_Agrupado2 = BaseSP_Agrupado2[colunas]

    ## Transformando a BaseSP_Agrupada2
    print(BaseSP_Agrupado2['Risco alagamento'].value_counts())
    BaseSP_Agrupado2[BaseSP_Agrupado2['Risco alagamento'] == 'Risco Crítico']
    BaseSP_Agrupado2[BaseSP_Agrupado2['Risco alagamento'] == 'Risco Elevado']
    BaseSP_Agrupado2 = BaseSP_Agrupado2.drop(columns=['Dia'])
    BaseSP_Agrupado2 = BaseSP_Agrupado2.drop(columns=['Estação (SP)'])


    altitude_map = {'Baixa': 1, 'Média': 2, 'Alta': 3}
    risco_alagamento_map = {'Sem Risco': 0, 'Risco Baixo': 1, 'Risco Moderado': 2, 'Risco Elevado': 3, 'Risco Crítico': 4}
    problemas_drenagem_map = {'Não': 0, 'Sim': 1}

    # Aplicando os mapeamentos nas colunas do DataFrame
    BaseSP_Agrupado2['Altitude'] = BaseSP_Agrupado2['Altitude'].map(altitude_map)
    BaseSP_Agrupado2['Risco alagamento'] = BaseSP_Agrupado2['Risco alagamento'].map(risco_alagamento_map)
    BaseSP_Agrupado2['Problemas de Drenagem'] = BaseSP_Agrupado2['Problemas de Drenagem'].map(problemas_drenagem_map)

    x_SP2 = BaseSP_Agrupado2.values # Dados todos em formato de matriz (Criando base temporária)

    SP_cols2 = list(BaseSP_Agrupado2.columns)
    SP_cols2 = [col for col in SP_cols2 if not any(keyword in col for keyword in ['Pressão', 'Temp', 'Umidade'])]
    SP_cols2 = [col for col in SP_cols2 if not col.startswith('Risco alagamento')]

    X_SP2 = BaseSP_Agrupado2[SP_cols2]
    y_SP2 = BaseSP_Agrupado2[[col for col in BaseSP_Agrupado2.columns if col.startswith('Risco alagamento')]]

    return X_SP2, y_SP2


def get_variaveis_RJ2024():

    ## Criando DataFrames que serão Agrupados (RJ)
    Teresopolis2 = pd.read_csv('Ambiente de teste-treinamento\RJ2024_Teresopolis_tratado')
    BaseTeresopolis2 = Teresopolis2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Duque_Caxias2 = pd.read_csv('Ambiente de teste-treinamento\RJ2024_DQC_tratado')
    BaseDuque2 = Duque_Caxias2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Goytacazes2 = pd.read_csv('Ambiente de teste-treinamento\RJ2024_Goytacazes_tratado')
    BaseGoytacazes2 = Goytacazes2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Macae2 = pd.read_csv('Ambiente de teste-treinamento\RJ2024_Macae_tratado')
    BaseMacae2 = Macae2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Niteroi2 = pd.read_csv('Ambiente de teste-treinamento\RJ2024_Niteroi_tratado')
    BaseNiteroi2 = Niteroi2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Nova_Friburgo2 = pd.read_csv('Ambiente de teste-treinamento\RJ2024_NovaFriburgo_tratado')
    BaseNovaFriburgo2= Nova_Friburgo2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Paraty2 = pd.read_csv('Ambiente de teste-treinamento\RJ2024_Paraty_tratado')
    BaseParaty2 = Paraty2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Rio_Claro2 = pd.read_csv('Ambiente de teste-treinamento\RJ2024_RioClaro_tratado')
    BaseRioClaro2 = Rio_Claro2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Angra2 = pd.read_csv('Ambiente de teste-treinamento\RJ2024_AngraReis_tratado')
    BaseAngra2 = Angra2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]


    ## Agrupando todos DataFrames (RJ)
    bases2 = [BaseDuque2, BaseGoytacazes2, BaseAngra2, BaseMacae2, BaseNiteroi2, BaseNovaFriburgo2, BaseParaty2, BaseRioClaro2, BaseTeresopolis2]
    nomes_estacoes2 = ['Duque_Caxias', 'Goytacazes', 'Angra_Reis', 'Macae', 'Niteroi', 'Nova_Friburgo', 'Paraty', 'Rio_Claro', 'Teresopolis']

    for df, nome2 in zip(bases2, nomes_estacoes2):
        df['Estação (RJ)'] = nome2

    BaseRJ_Agrupado2 = pd.concat(bases2, ignore_index=True)
    colunas = ['Estação (RJ)'] + [col for col in BaseRJ_Agrupado2.columns if col != 'Estação (RJ)']
    BaseRJ_Agrupado2 = BaseRJ_Agrupado2[colunas]


    ## Transformando a BaseRJ_Agrupada2

    BaseRJ_Agrupado2 = BaseRJ_Agrupado2.drop(columns=['Dia'])
    BaseRJ_Agrupado2 = BaseRJ_Agrupado2.drop(columns=['Estação (RJ)'])


    altitude_map = {'Baixa': 1, 'Média': 2, 'Alta': 3}
    risco_alagamento_map = {'Sem Risco': 0, 'Risco Baixo': 1, 'Risco Moderado': 2, 'Risco Elevado': 3, 'Risco Crítico': 4}
    problemas_drenagem_map = {'Não': 0, 'Sim': 1}

    # Aplicando os mapeamentos nas colunas do DataFrame
    BaseRJ_Agrupado2['Altitude'] = BaseRJ_Agrupado2['Altitude'].map(altitude_map)
    BaseRJ_Agrupado2['Risco alagamento'] = BaseRJ_Agrupado2['Risco alagamento'].map(risco_alagamento_map)
    BaseRJ_Agrupado2['Problemas de Drenagem'] = BaseRJ_Agrupado2['Problemas de Drenagem'].map(problemas_drenagem_map)


    x_RJ2 = BaseRJ_Agrupado2.values # Dados todos em formato de matriz (Criando base temporária)

    RJ_cols2 = list(BaseRJ_Agrupado2.columns)
    RJ_cols2 = [col for col in RJ_cols2 if not any(keyword in col for keyword in ['Pressão', 'Temp', 'Umidade'])]
    RJ_cols2 = [col for col in RJ_cols2 if not col.startswith('Risco alagamento')]

    X_RJ2 = BaseRJ_Agrupado2[RJ_cols2]
    y_RJ2 = BaseRJ_Agrupado2[[col for col in BaseRJ_Agrupado2.columns if col.startswith('Risco alagamento')]]

    return X_RJ2, y_RJ2


def get_variaveis_MG2024():

        ## Criando DataFrames que serão Agrupados (MG)
    Belo_Horizonte2 = pd.read_csv('Ambiente de teste-treinamento\MG2024_Belo_Horizonte_tratado')
    BaseBH2 = Belo_Horizonte2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Caldas2 = pd.read_csv('Ambiente de teste-treinamento\MG2024_Caldas_tratado')
    BaseCaldas2 = Caldas2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Juiz_de_Fora2 = pd.read_csv('Ambiente de teste-treinamento\MG2024_JFC_tratado')
    BaseJuiz2 = Juiz_de_Fora2[[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Machado2 = pd.read_csv('Ambiente de teste-treinamento\MG2024_Machado_tratado')
    BaseMachado2 = Machado2[[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Monte_verde2 = pd.read_csv('Ambiente de teste-treinamento\MG2024_MonVerde_tratado')
    BaseMonte2 = Monte_verde2[[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Passa_quatro2 = pd.read_csv('Ambiente de teste-treinamento\MG2024_P4_tratado')
    BaseP42 = Passa_quatro2[[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Sao_Joao2 = pd.read_csv('Ambiente de teste-treinamento\MG2024_Sao_Joao_del_Rei_tratado')
    BaseSJ2 = Sao_Joao2[[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Teofilo2 = pd.read_csv('Ambiente de teste-treinamento\MG2024_Teofilo_Otoni_tratado')
    BaseTeofilo2 = Teofilo2[[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Uberaba2 = pd.read_csv('Ambiente de teste-treinamento\MG2024_Uberaba_tratado')
    BaseUberaba2 = Uberaba2[[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Uberlandia2 = pd.read_csv('Ambiente de teste-treinamento\MG2024_Uberlandia_tratado')
    BaseUberlandia2 = Uberlandia2[[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]


    ## Agrupando todos DataFrames (MG)
    bases2 = [BaseBH2, BaseCaldas2, BaseJuiz2, BaseMachado2, BaseUberaba2, BaseMonte2, BaseP42, BaseSJ2, BaseTeofilo2, BaseUberlandia2]
    nomes_estacoes2 = ['Belo_Horizonte', 'Caldas', 'Juiz_Fora', 'Machado', 'Uberaba', 'Monte_Verde', 'Passa_Quatro', 'SJ_Del_Rei', 'Teofilo', 'Uberlandia']

    for df, nome2 in zip(bases2, nomes_estacoes2):
        df['Estação (MG)'] = nome2

    BaseMG_Agrupado2 = pd.concat(bases2, ignore_index=True)

    colunas = ['Estação (MG)'] + [col for col in BaseMG_Agrupado2.columns if col != 'Estação (MG)']
    BaseMG_Agrupado2 = BaseMG_Agrupado2[colunas]


    ## Transformando a BaseMG_Agrupada2

    BaseMG_Agrupado2 = BaseMG_Agrupado2.drop(columns=['Dia'])
    BaseMG_Agrupado2 = BaseMG_Agrupado2.drop(columns=['Estação (MG)'])


    altitude_map = {'Baixa': 1, 'Média': 2, 'Alta': 3}
    risco_alagamento_map = {'Sem Risco': 0, 'Risco Baixo': 1, 'Risco Moderado': 2, 'Risco Elevado': 3, 'Risco Crítico': 4}
    problemas_drenagem_map = {'Não': 0, 'Sim': 1}

    # Aplicando os mapeamentos nas colunas do DataFrame
    BaseMG_Agrupado2['Altitude'] = BaseMG_Agrupado2['Altitude'].map(altitude_map)
    BaseMG_Agrupado2['Risco alagamento'] = BaseMG_Agrupado2['Risco alagamento'].map(risco_alagamento_map)
    BaseMG_Agrupado2['Problemas de Drenagem'] = BaseMG_Agrupado2['Problemas de Drenagem'].map(problemas_drenagem_map)


    x_MG2 = BaseMG_Agrupado2.values # Dados todos em formato de matriz (Criando base temporária)


    # Filtrando as colunas relevantes em MG
    MG_cols2 = list(BaseMG_Agrupado2.columns)

    # Removendo colunas que contêm palavras-chave específicas
    MG_cols2 = [col for col in MG_cols2 if not any(keyword in col for keyword in ['Pressão', 'Temp', 'Umidade'])]

    # Removendo colunas que começam com "Risco alagamento"
    MG_cols2 = [col for col in MG_cols2 if not col.startswith('Risco alagamento')]

    # Criando os conjuntos X e y
    X_MG2 = BaseMG_Agrupado2[MG_cols2]
    y_MG2 = BaseMG_Agrupado2[[col for col in BaseMG_Agrupado2.columns if col.startswith('Risco alagamento')]]

    return X_MG2, y_MG2


def get_variaveis_SC2024():
    ## Criando DataFrames que serão Agrupados (SC)

    Bom_Jardim2 = pd.read_csv('Ambiente de teste-treinamento\SC2024_Bom Jardim da Serra_tratado')
    BaseBom_Jardim2 = Bom_Jardim2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Florianopolis2 = pd.read_csv('Ambiente de teste-treinamento\SC2024_Florianopolis_tratado')
    BaseFlorianopolis2 = Florianopolis2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Indaial2 = pd.read_csv('Ambiente de teste-treinamento\SC2024_Indaial_tratado')
    BaseIndaial2 = Indaial2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Itajai2 = pd.read_csv('Ambiente de teste-treinamento\SC2024_Itajai_tratado')
    BaseItajai2 = Itajai2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Itapoa2 = pd.read_csv('Ambiente de teste-treinamento\SC2024_Itapoa_tratado')
    BaseItapoa2 = Itapoa2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Ituporanga2 = pd.read_csv('Ambiente de teste-treinamento\SC2024_Ituporanga_tratado')
    BaseItuporanga2 = Ituporanga2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Rio_Negro2 = pd.read_csv('Ambiente de teste-treinamento\SC2024_Rio Negro_tratado')
    BaseRio_Negro2 = Rio_Negro2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Rio_Campo2 = pd.read_csv('Ambiente de teste-treinamento\SC2024_Rio do Campo_tratado')
    BaseRio_Campo2 = Rio_Campo2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Pinhais2 = pd.read_csv('Ambiente de teste-treinamento\SC2024_São José dos Pinhais_tratado')
    BasePinhais2 = Pinhais2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Urussanga2 = pd.read_csv('Ambiente de teste-treinamento\SC2024_Urussanga_tratado')
    BaseUrussanga2 = Urussanga2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Xanxare2 = pd.read_csv('Ambiente de teste-treinamento\SC2024_Xanxere_tratado')
    BaseXanxare2  = Xanxare2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]


    ## Agrupando todos DataFrames (SC)
    # Novas bases e nomes das estações
    bases2 = [BaseBom_Jardim2, BaseFlorianopolis2, BaseIndaial2, BaseItajai2, BaseItapoa2, BaseItuporanga2, BaseRio_Negro2, BaseRio_Campo2, BasePinhais2, BaseUrussanga2, BaseXanxare2]
    nomes_estacoes2 = ['Bom_Jardim', 'Florianopolis', 'Indaial', 'Itajai', 'Itapoa', 'Ituporanga', 'Rio_Negro', 'Rio_Campo', 'Pinhais', 'Urussanga', 'Xanxare']

    # Atribuindo o nome da estação a cada DataFrame na lista 'bases'
    for df, nome2 in zip(bases2, nomes_estacoes2):
        df['Estação (SC)'] = nome2

    # Concatenando todos os DataFrames em um único DataFrame
    BaseSC_Agrupado2 = pd.concat(bases2, ignore_index=True)

    colunas = ['Estação (SC)'] + [col for col in BaseSC_Agrupado2.columns if col != 'Estação (SC)']
    BaseSC_Agrupado2 = BaseSC_Agrupado2[colunas]


    ## Transformando a BaseSC_Agrupada2

    BaseSC_Agrupado2[BaseSC_Agrupado2['Risco alagamento'] == 'Risco Crítico']
    BaseSC_Agrupado2[BaseSC_Agrupado2['Risco alagamento'] == 'Risco Elevado']
    BaseSC_Agrupado2 = BaseSC_Agrupado2.drop(columns=['Dia'])
    BaseSC_Agrupado2 = BaseSC_Agrupado2.drop(columns=['Estação (SC)'])

    altitude_map = {'Baixa': 1, 'Média': 2, 'Alta': 3}
    risco_alagamento_map = {'Sem Risco': 0, 'Risco Baixo': 1, 'Risco Moderado': 2, 'Risco Elevado': 3, 'Risco Crítico': 4}
    problemas_drenagem_map = {'Não': 0, 'Sim': 1}

    # Aplicando os mapeamentos nas colunas do DataFrame
    BaseSC_Agrupado2['Altitude'] = BaseSC_Agrupado2['Altitude'].map(altitude_map)
    BaseSC_Agrupado2['Risco alagamento'] = BaseSC_Agrupado2['Risco alagamento'].map(risco_alagamento_map)
    BaseSC_Agrupado2['Problemas de Drenagem'] = BaseSC_Agrupado2['Problemas de Drenagem'].map(problemas_drenagem_map)


    x_SC2 = BaseSC_Agrupado2.values # Dados todos em formato de matriz (Criando base temporária)


    # Filtrando as colunas relevantes em SC
    SC_cols2 = list(BaseSC_Agrupado2.columns)

    # Removendo colunas que contêm palavras-chave específicas
    SC_cols2 = [col for col in SC_cols2 if not any(keyword in col for keyword in ['Pressão', 'Temp', 'Umidade'])]

    # Removendo colunas que começam com "Risco alagamento"
    SC_cols2 = [col for col in SC_cols2 if not col.startswith('Risco alagamento')]

    # Criando os conjuntos X e y
    X_SC2 = BaseSC_Agrupado2[SC_cols2]
    y_SC2 = BaseSC_Agrupado2[[col for col in BaseSC_Agrupado2.columns if col.startswith('Risco alagamento')]]

    return X_SC2, y_SC2


def get_variaveis_RS2024():

        ## Criando DataFrames que serão Agrupados (RS)
    Alegrete2 = pd.read_csv('Ambiente de teste-treinamento\RS2024_Alegrete_tratado')
    BaseAlegrete2 = Alegrete2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    CBom2 = pd.read_csv('Ambiente de teste-treinamento\RS2024_CBom_tratado')
    BaseCampoBom2 = CBom2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    CaLe2 = pd.read_csv('Ambiente de teste-treinamento\RS2024_CaLe_tratado')
    BaseCapaoLeao2 = CaLe2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    camaqua2 = pd.read_csv('Ambiente de teste-treinamento\RS2024_Camaqua_tratado')
    BaseCamaqua2 = camaqua2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Cangucu2 = pd.read_csv('Ambiente de teste-treinamento\RS2024_Cangucu_tratado')
    BaseCangucu2 = Cangucu2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Dom_Pedritoo2 = pd.read_csv('Ambiente de teste-treinamento\RS2024_Dom Pedrito_tratado')
    BaseDomPedrito2 = Dom_Pedritoo2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Jaguarao2 = pd.read_csv('Ambiente de teste-treinamento\RS2024_Jaguarão_tratado')
    BaseJaguarao2 = Jaguarao2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Mostardas2 = pd.read_csv('Ambiente de teste-treinamento\RS2024_Mostardas_tratado')
    BaseMostardas2 = Mostardas2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    pAlegre2 = pd.read_csv('Ambiente de teste-treinamento\RS2024_PAlegre_tratado')
    BasePortoAlegre2 = pAlegre2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Sao_Gabriel2 = pd.read_csv('Ambiente de teste-treinamento\RS2024_São Gabriel_tratado')
    BaseSaoGabriel2 = Sao_Gabriel2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Uruguaiana2 = pd.read_csv('Ambiente de teste-treinamento\RS2024_Uruguaiana_tratado')
    BaseUruguaiana2 = Uruguaiana2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]


    ## Agrupando todos DataFrames (RS)
    # Novas bases e nomes das estações
    bases2 = [BaseAlegrete2, BaseCampoBom2, BaseCapaoLeao2, BaseCamaqua2, BaseCangucu2, BaseDomPedrito2, BaseJaguarao2, BaseMostardas2, BasePortoAlegre2, BaseSaoGabriel2, BaseUruguaiana2]
    nomes_estacoes2 = ['Alegrete', 'Campo_Bom', 'Capao_Leao', 'Camaqua', 'Cangucu', 'Dom_Pedrito', 'Jaguarao', 'Mostardas', 'Porto_Alegre', 'Sao_Gabriel', 'Uruguaiana']

    # Atribuindo o nome da estação a cada DataFrame na lista 'bases'
    for df, nome2 in zip(bases2, nomes_estacoes2):
        df['Estação (RS)'] = nome2

    # Concatenando todos os DataFrames em um único DataFrame
    BaseRS_Agrupado2 = pd.concat(bases2, ignore_index=True)

    colunas = ['Estação (RS)'] + [col for col in BaseRS_Agrupado2.columns if col != 'Estação (RS)']
    BaseRS_Agrupado2 = BaseRS_Agrupado2[colunas]


    ## Transformando a BaseRS_Agrupada2

    BaseRS_Agrupado2 = BaseRS_Agrupado2.drop(columns=['Dia'])
    BaseRS_Agrupado2 = BaseRS_Agrupado2.drop(columns=['Estação (RS)'])


    altitude_map = {'Baixa': 1, 'Média': 2, 'Alta': 3}
    risco_alagamento_map = {'Sem Risco': 0, 'Risco Baixo': 1, 'Risco Moderado': 2, 'Risco Elevado': 3, 'Risco Crítico': 4}
    problemas_drenagem_map = {'Não': 0, 'Sim': 1}

    # Aplicando os mapeamentos nas colunas do DataFrame
    BaseRS_Agrupado2['Altitude'] = BaseRS_Agrupado2['Altitude'].map(altitude_map)
    BaseRS_Agrupado2['Risco alagamento'] = BaseRS_Agrupado2['Risco alagamento'].map(risco_alagamento_map)
    BaseRS_Agrupado2['Problemas de Drenagem'] = BaseRS_Agrupado2['Problemas de Drenagem'].map(problemas_drenagem_map)


    x_RS2 = BaseRS_Agrupado2.values # Dados todos em formato de matriz (Criando base temporária)


    # Filtrando as colunas relevantes em RS
    RS_cols2 = list(BaseRS_Agrupado2.columns)

    # Removendo colunas que contêm palavras-chave específicas
    RS_cols2 = [col for col in RS_cols2 if not any(keyword in col for keyword in ['Pressão', 'Temp', 'Umidade'])]

    # Removendo colunas que começam com "Risco alagamento"
    RS_cols2 = [col for col in RS_cols2 if not col.startswith('Risco alagamento')]

    # Criando os conjuntos X e y
    X_RS2 = BaseRS_Agrupado2[RS_cols2]
    y_RS2 = BaseRS_Agrupado2[[col for col in BaseRS_Agrupado2.columns if col.startswith('Risco alagamento')]]

    return X_RS2, y_RS2


def get_variaveis_PR2024():

        ## Criando DataFrames que serão Agrupados (PR)
    Colombo2 = pd.read_csv('Ambiente de teste-treinamento\PR2024_Colombo_tratado')
    BaseColombo2 = Colombo2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Curitiba2 = pd.read_csv('Ambiente de teste-treinamento\PR2024_Curitiba_tratado')
    BaseCuritiba2 = Curitiba2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Dois_Vizinhos2 = pd.read_csv('Ambiente de teste-treinamento\PR2024_Dois Vizinhos_tratado')
    BaseDois_Vizinhos2 = Dois_Vizinhos2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    General_carneiro2 = pd.read_csv('Ambiente de teste-treinamento\PR2024_General Carneiro_tratado')
    BaseGeneral_Carneiro2 = General_carneiro2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Goiania2 = pd.read_csv('Ambiente de teste-treinamento\PR2024_Goiânia_tratado')
    BaseGoiania2 = Goiania2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Icaraima2 = pd.read_csv('Ambiente de teste-treinamento\PR2024_Icaraima_tratado')
    BaseIcaraima2 = Icaraima2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Joao_Tavares2 = pd.read_csv('Ambiente de teste-treinamento\PR2024_João_Tavares_tratado')
    BaseJoao_Tavares2 = Joao_Tavares2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Maringa2 = pd.read_csv('Ambiente de teste-treinamento\PR2024_Maringá_tratado')
    BaseMaringa2 = Maringa2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Morretes2 = pd.read_csv('Ambiente de teste-treinamento\PR2024_Morro_tratado')
    BaseMorretes2 = Morretes2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]

    Sao_Matheus2 = pd.read_csv('Ambiente de teste-treinamento\PR2024_São Mateus do Sul_tratado')
    BaseSao_Matheus2 = Sao_Matheus2 [[
        'Dia',
        'Precipitação (mm)',
        'Pressão Média (mB)',
        'Temp Ponto Orvalho (°C)',
        'Umidade Média (%)',
        'Cobertura Vegetal (%)',
        'Altitude',
        'Problemas de Drenagem',
        'Risco alagamento',
    ]]



    ## Agrupando todos DataFrames (PR)
    # Novas bases e nomes das estações
    bases2 = [BaseColombo2, BaseCuritiba2, BaseDois_Vizinhos2, BaseGeneral_Carneiro2, BaseGoiania2, BaseIcaraima2, BaseJoao_Tavares2, BaseMaringa2, BaseMorretes2, BaseSao_Matheus2]
    nomes_estacoes2 = ['Colombo', 'Curitiba', 'Dois_Vizinhos', 'General_Carneiro', 'Goiania', 'Icaraima', 'Joao_Tavares', 'Maringa', 'Morretes', 'Sao_Matheus']

    # Atribuindo o nome da estação a cada DataFrame na lista 'bases'
    for df, nome2 in zip(bases2, nomes_estacoes2):
        df['Estação (PR)'] = nome2

    # Concatenando todos os DataFrames em um único DataFrame
    BasePR_Agrupado2 = pd.concat(bases2, ignore_index=True)

    colunas = ['Estação (PR)'] + [col for col in BasePR_Agrupado2.columns if col != 'Estação (PR)']
    BasePR_Agrupado2 = BasePR_Agrupado2[colunas]


    ## Transformando a BasePR_Agrupada2
    BasePR_Agrupado2 = BasePR_Agrupado2.drop(columns=['Dia'])
    BasePR_Agrupado2 = BasePR_Agrupado2.drop(columns=['Estação (PR)'])


    altitude_map = {'Baixa': 1, 'Média': 2, 'Alta': 3}
    risco_alagamento_map = {'Sem Risco': 0, 'Risco Baixo': 1, 'Risco Moderado': 2, 'Risco Elevado': 3, 'Risco Crítico': 4}
    problemas_drenagem_map = {'Não': 0, 'Sim': 1}

    # Aplicando os mapeamentos nas colunas do DataFrame
    BasePR_Agrupado2['Altitude'] = BasePR_Agrupado2['Altitude'].map(altitude_map)
    BasePR_Agrupado2['Risco alagamento'] = BasePR_Agrupado2['Risco alagamento'].map(risco_alagamento_map)
    BasePR_Agrupado2['Problemas de Drenagem'] = BasePR_Agrupado2['Problemas de Drenagem'].map(problemas_drenagem_map)


    x_PR2 = BasePR_Agrupado2.values # Dados todos em formato de matriz (Criando base temporária)


    # Filtrando as colunas relevantes em PR
    PR_cols2 = list(BasePR_Agrupado2.columns)

    # Removendo colunas que contêm palavras-chave específicas
    PR_cols2 = [col for col in PR_cols2 if not any(keyword in col for keyword in ['Pressão', 'Temp', 'Umidade'])]

    # Removendo colunas que começam com "Risco alagamento"
    PR_cols2 = [col for col in PR_cols2 if not col.startswith('Risco alagamento')]

    # Criando os conjuntos X e y
    X_PR2 = BasePR_Agrupado2[PR_cols2]
    y_PR2 = BasePR_Agrupado2[[col for col in BasePR_Agrupado2.columns if col.startswith('Risco alagamento')]]

    return X_PR2, y_PR2