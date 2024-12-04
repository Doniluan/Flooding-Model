import pandas as pd



def get_variaveis_SP2023():
## Criando DataFrames que serão Agrupados (SP)

    Braganca = pd.read_csv('Ambiente de teste-treinamento/SP_BP_tratado')
    BaseBraganca = Braganca [[
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


    Bertioga = pd.read_csv('Ambiente de teste-treinamento/SP_Bertioga_tratado')
    BaseBertioga = Bertioga [[
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


    Barueri = pd.read_csv('Ambiente de teste-treinamento/SP_Barueri_tratado')
    BaseBarueri = Barueri [[
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


    Iguape = pd.read_csv('Ambiente de teste-treinamento/SP_Iguapê_tratado')
    BaseIguape = Iguape [[
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

    Taubate = pd.read_csv('Ambiente de teste-treinamento/SP_Taubate_tratado')
    BaseTaubate = Taubate [[
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

    SP = pd.read_csv('Ambiente de teste-treinamento/SP_tratado')
    BaseInterlagos = SP [[
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


    SLP = pd.read_csv('Ambiente de teste-treinamento/SP_SLP_tratado')
    BaseSLP = SLP [[
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

    Registro = pd.read_csv('Ambiente de teste-treinamento/SP_Registro_tratado')
    BaseRegistro = Registro [[
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

    Piracicaba = pd.read_csv('Ambiente de teste-treinamento/SP_Piracicaba_tratado')
    BasePira = Piracicaba [[
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
    bases = [BaseBraganca, BaseBertioga, BaseBarueri, BaseTaubate, BasePira, BaseRegistro, BaseInterlagos, BaseIguape, BaseSLP]
    nomes_estacoes = ['Braganca', 'Bertioga', 'Barueri', 'Taubate', 'Piracicaba', 'Registro', 'Interlagos', 'Iguape', 'São Luiz']


    for df, nome in zip(bases, nomes_estacoes):
        df['Estação (SP)'] = nome


    BaseSP_Agrupado = pd.concat(bases, ignore_index=True)
    colunas = ['Estação (SP)'] + [col for col in BaseSP_Agrupado.columns if col != 'Estação (SP)']
    BaseSP_Agrupado = BaseSP_Agrupado[colunas]


    ## Transformando a BaseSP_Agrupada
    BaseSP_Agrupado = BaseSP_Agrupado.drop(columns=['Dia'])
    BaseSP_Agrupado = BaseSP_Agrupado.drop(columns=['Estação (SP)'])

    altitude_map = {'Baixa': 1, 'Média': 2, 'Alta': 3}
    risco_alagamento_map = {'Sem Risco': 0, 'Risco Baixo': 1, 'Risco Moderado': 2, 'Risco Elevado': 3, 'Risco Crítico': 4}
    problemas_drenagem_map = {'Não': 0, 'Sim': 1}

    # Aplicando os mapeamentos nas colunas do DataFrame
    BaseSP_Agrupado['Altitude'] = BaseSP_Agrupado['Altitude'].map(altitude_map)
    BaseSP_Agrupado['Risco alagamento'] = BaseSP_Agrupado['Risco alagamento'].map(risco_alagamento_map)
    BaseSP_Agrupado['Problemas de Drenagem'] = BaseSP_Agrupado['Problemas de Drenagem'].map(problemas_drenagem_map)

    SP_cols = list(BaseSP_Agrupado.columns)
    SP_cols = [col for col in SP_cols if not any(keyword in col for keyword in ['Pressão', 'Temp', 'Umidade'])]
    SP_cols = [col for col in SP_cols if not col.startswith('Risco alagamento')]
    X_SP = BaseSP_Agrupado[SP_cols]
    y_SP = BaseSP_Agrupado[[col for col in BaseSP_Agrupado.columns if col.startswith('Risco alagamento')]]

    return X_SP, y_SP


def get_variaveis_RJ2023():

    ## Criando DataFrames que serão Agrupados (RJ)
    Duque_Caxias = pd.read_csv('Ambiente de teste-treinamento/RJ_DQC_tratado')
    BaseDuque = Duque_Caxias [[
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


    Goytacazes = pd.read_csv('Ambiente de teste-treinamento/RJ_Goytacazes_tratado')
    BaseGoytacazes = Goytacazes [[
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


    Angra_dos_Reis = pd.read_csv('Ambiente de teste-treinamento/RJ_AngraReis_tratado')
    BaseAngra = Angra_dos_Reis [[
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


    Macae = pd.read_csv('Ambiente de teste-treinamento/RJ_Macae_tratado')
    BaseMacae = Macae [[
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


    Niteroi = pd.read_csv('Ambiente de teste-treinamento/RJ_Niteroi_tratado')
    BaseNiteroi = Niteroi [[
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


    Nova_Friburgo = pd.read_csv('Ambiente de teste-treinamento/RJ_NovaFriburgo_tratado')
    BaseNovaFriburgo = Nova_Friburgo [[
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


    Paraty = pd.read_csv('Ambiente de teste-treinamento/RJ_Paraty_tratado')
    BaseParaty = Paraty [[
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


    Rio_Claro = pd.read_csv('Ambiente de teste-treinamento/RJ_RioClaro_tratado')
    BaseRioClaro = Rio_Claro [[
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


    Teresopolis = pd.read_csv('Ambiente de teste-treinamento/RJ_Teresopolis_tratado')
    BaseTeresopolis = Teresopolis [[
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
    bases = [BaseDuque, BaseGoytacazes, BaseAngra, BaseMacae, BaseNiteroi, BaseNovaFriburgo, BaseParaty, BaseRioClaro, BaseTeresopolis]
    nomes_estacoes = ['Duque_Caxias', 'Goytacazes', 'Angra_Reis', 'Macae', 'Niteroi', 'Nova_Friburgo', 'Paraty', 'Rio_Claro', 'Teresopolis']


    for df, nome in zip(bases, nomes_estacoes):
        df['Estação (RJ)'] = nome


    BaseRJ_Agrupado = pd.concat(bases, ignore_index=True)
    colunas = ['Estação (RJ)'] + [col for col in BaseRJ_Agrupado.columns if col != 'Estação (RJ)']
    BaseRJ_Agrupado = BaseRJ_Agrupado[colunas]




    BaseRJ_Agrupado = BaseRJ_Agrupado.drop(columns=['Dia'])
    BaseRJ_Agrupado = BaseRJ_Agrupado.drop(columns=['Estação (RJ)'])


    altitude_map = {'Baixa': 1, 'Média': 2, 'Alta': 3}
    risco_alagamento_map = {'Sem Risco': 0, 'Risco Baixo': 1, 'Risco Moderado': 2, 'Risco Elevado': 3, 'Risco Crítico': 4}
    problemas_drenagem_map = {'Não': 0, 'Sim': 1}

    # Aplicando os mapeamentos nas colunas do DataFrame
    BaseRJ_Agrupado['Altitude'] = BaseRJ_Agrupado['Altitude'].map(altitude_map)
    BaseRJ_Agrupado['Risco alagamento'] = BaseRJ_Agrupado['Risco alagamento'].map(risco_alagamento_map)
    BaseRJ_Agrupado['Problemas de Drenagem'] = BaseRJ_Agrupado['Problemas de Drenagem'].map(problemas_drenagem_map)

    x_RJ = BaseRJ_Agrupado.values # Dados todos em formato de matriz (Criando base temporária)

    RJ_cols = list(BaseRJ_Agrupado.columns)
    RJ_cols = [col for col in RJ_cols if not any(keyword in col for keyword in ['Pressão', 'Temp', 'Umidade'])]
    RJ_cols = [col for col in RJ_cols if not col.startswith('Risco alagamento')]

    X_RJ = BaseRJ_Agrupado[RJ_cols]
    y_RJ = BaseRJ_Agrupado[[col for col in BaseRJ_Agrupado.columns if col.startswith('Risco alagamento')]]

    return X_RJ, y_RJ


def get_variaveis_MG2023():

    ## Criando DataFrames que serão Agrupados (MG)
    Belo_Horizonte = pd.read_csv('Ambiente de teste-treinamento/MG_Belo_Horizonte_tratado')
    BaseBH = Belo_Horizonte [[
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

    Caldas = pd.read_csv('Ambiente de teste-treinamento/MG_Caldas_tratado')
    BaseCaldas = Caldas [[
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

    Juiz_de_Fora = pd.read_csv('Ambiente de teste-treinamento/MG_JFC_tratado')
    BaseJuiz = Juiz_de_Fora[[
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

    Machado = pd.read_csv('Ambiente de teste-treinamento/MG_Machado_tratado')
    BaseMachado = Machado[[
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

    Monte_verder = pd.read_csv('Ambiente de teste-treinamento/MG_MonVerde_tratado')
    BaseMonte = Monte_verder[[
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

    Passa_quatro = pd.read_csv('Ambiente de teste-treinamento/MG_P4_tratado')
    BaseP4 = Passa_quatro[[
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

    Sao_Joao = pd.read_csv('Ambiente de teste-treinamento/MG_Sao_Joao_del_Rei_tratado')
    BaseSJ = Sao_Joao[[
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

    Teofilo = pd.read_csv('Ambiente de teste-treinamento/MG_Teofilo_Otoni_tratado')
    BaseTeofilo = Teofilo[[
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

    Uberaba = pd.read_csv('Ambiente de teste-treinamento/MG_Uberaba_tratado')
    BaseUberaba = Uberaba[[
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

    Uberlandia = pd.read_csv('Ambiente de teste-treinamento/MG_Uberlandia_tratado')
    BaseUberlandia = Uberlandia[[
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
    bases = [BaseBH, BaseCaldas, BaseJuiz, BaseMachado, BaseUberaba, BaseMonte, BaseP4, BaseSJ, BaseTeofilo, BaseUberlandia]
    nomes_estacoes = ['Belo_Horizonte', 'Caldas', 'Juiz_Fora', 'Machado', 'Uberaba', 'Monte_Verde', 'Passa_Quatro', 'SJ_Del_Rei', 'Teofilo', 'Uberlandia']


    for df, nome in zip(bases, nomes_estacoes):
        df['Estação (MG)'] = nome


    BaseMG_Agrupado = pd.concat(bases, ignore_index=True)
    colunas = ['Estação (MG)'] + [col for col in BaseMG_Agrupado.columns if col != 'Estação (MG)']
    BaseMG_Agrupado = BaseMG_Agrupado[colunas]


    ## Transformando a BaseMG_Agrupada

    BaseMG_Agrupado = BaseMG_Agrupado.drop(columns=['Dia'])
    BaseMG_Agrupado = BaseMG_Agrupado.drop(columns=['Estação (MG)'])



    altitude_map = {'Baixa': 1, 'Média': 2, 'Alta': 3}
    risco_alagamento_map = {'Sem Risco': 0, 'Risco Baixo': 1, 'Risco Moderado': 2, 'Risco Elevado': 3, 'Risco Crítico': 4}
    problemas_drenagem_map = {'Não': 0, 'Sim': 1}

    # Aplicando os mapeamentos nas colunas do DataFrame
    BaseMG_Agrupado['Altitude'] = BaseMG_Agrupado['Altitude'].map(altitude_map)
    BaseMG_Agrupado['Risco alagamento'] = BaseMG_Agrupado['Risco alagamento'].map(risco_alagamento_map)
    BaseMG_Agrupado['Problemas de Drenagem'] = BaseMG_Agrupado['Problemas de Drenagem'].map(problemas_drenagem_map)

    x_MG = BaseMG_Agrupado.values # Dados todos em formato de matriz (Criando base temporária)

    MG_cols = list(BaseMG_Agrupado.columns)
    MG_cols = [col for col in MG_cols if not any(keyword in col for keyword in ['Pressão', 'Temp', 'Umidade'])]
    MG_cols = [col for col in MG_cols if not col.startswith('Risco alagamento')]

    x_MG = BaseMG_Agrupado[MG_cols]
    y_MG = BaseMG_Agrupado[[col for col in BaseMG_Agrupado.columns if col.startswith('Risco alagamento')]]


    return x_MG, y_MG


def get_variaveis_SC2023():

    ## Criando DataFrames que serão Agrupados (SC)
    Bom_Jardim = pd.read_csv('Ambiente de teste-treinamento/SC_Bom Jardim da Serra_tratado')
    BaseBom_Jardim = Bom_Jardim [[
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


    Florianopolis = pd.read_csv('Ambiente de teste-treinamento/SC_Florianopolis_tratado')
    BaseFlorianopolis = Florianopolis [[
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


    Indaial = pd.read_csv('Ambiente de teste-treinamento/SC_Indaial_tratado')
    BaseIndaial = Indaial [[
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


    Itajai = pd.read_csv('Ambiente de teste-treinamento/SC_Itajai_tratado')
    BaseItajai = Itajai [[
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


    Itapoa = pd.read_csv('Ambiente de teste-treinamento/SC_Itapoa_tratado')
    BaseItapoa = Itapoa [[
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


    Ituporanga = pd.read_csv('Ambiente de teste-treinamento/SC_Ituporanga_tratado')
    BaseItuporanga = Ituporanga [[
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


    Rio_Negro = pd.read_csv('Ambiente de teste-treinamento/SC_Rio Negro_tratado')
    BaseRio_Negro = Rio_Negro [[
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


    Rio_Campo = pd.read_csv('Ambiente de teste-treinamento/SC_Rio do Campo_tratado')
    BaseRio_Campo = Rio_Campo [[
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


    Pinhais = pd.read_csv('Ambiente de teste-treinamento/SC_São José dos Pinhais_tratado')
    BasePinhais = Pinhais [[
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


    Urussanga = pd.read_csv('Ambiente de teste-treinamento/SC_Urussanga_tratado')
    BaseUrussanga = Urussanga [[
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


    Xanxare = pd.read_csv('Ambiente de teste-treinamento/SC_Xanxere_tratado')
    BaseXanxare  = Xanxare [[
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
    bases = [BaseBom_Jardim, BaseFlorianopolis, BaseIndaial, BaseItajai, BaseItapoa, BaseItuporanga, BaseRio_Negro, BaseRio_Campo, BasePinhais, BaseUrussanga, BaseXanxare]
    nomes_estacoes = ['Bom_Jardim', 'Florianopolis', 'Indaial', 'Itajai', 'Itapoa', 'Ituporanga', 'Rio_Negro', 'Rio_Campo', 'Pinhais', 'Urussanga', 'Xanxare']

    # Atribuindo o nome da estação a cada DataFrame na lista 'bases'
    for df, nome in zip(bases, nomes_estacoes):
        df['Estação (SC)'] = nome

    # Concatenando todos os DataFrames em um único DataFrame
    BaseSC_Agrupado = pd.concat(bases, ignore_index=True)

    colunas = ['Estação (SC)'] + [col for col in BaseSC_Agrupado.columns if col != 'Estação (SC)']
    BaseSC_Agrupado = BaseSC_Agrupado[colunas]


    ## Transformando a BaseSC_Agrupada
    BaseSC_Agrupado = BaseSC_Agrupado.drop(columns=['Dia'])
    BaseSC_Agrupado = BaseSC_Agrupado.drop(columns=['Estação (SC)'])


    altitude_map = {'Baixa': 1, 'Média': 2, 'Alta': 3}
    risco_alagamento_map = {'Sem Risco': 0, 'Risco Baixo': 1, 'Risco Moderado': 2, 'Risco Elevado': 3, 'Risco Crítico': 4}
    problemas_drenagem_map = {'Não': 0, 'Sim': 1}

    # Aplicando os mapeamentos nas colunas do DataFrame
    BaseSC_Agrupado['Altitude'] = BaseSC_Agrupado['Altitude'].map(altitude_map)
    BaseSC_Agrupado['Risco alagamento'] = BaseSC_Agrupado['Risco alagamento'].map(risco_alagamento_map)
    BaseSC_Agrupado['Problemas de Drenagem'] = BaseSC_Agrupado['Problemas de Drenagem'].map(problemas_drenagem_map)

    x_SC = BaseSC_Agrupado.values # Dados todos em formato de matriz (Criando base temporária)

    SC_cols = list(BaseSC_Agrupado.columns)
    SC_cols = [col for col in SC_cols if not any(keyword in col for keyword in ['Pressão', 'Temp', 'Umidade'])]
    SC_cols = [col for col in SC_cols if not col.startswith('Risco alagamento')]

    x_SC = BaseSC_Agrupado[SC_cols]
    y_SC = BaseSC_Agrupado[[col for col in BaseSC_Agrupado.columns if col.startswith('Risco alagamento')]]

    return x_SC, y_SC


def get_variaveis_RS2023():

    ## Criando DataFrames que serão Agrupados (RS)
    Alegrete = pd.read_csv('Ambiente de teste-treinamento/RS_Alegrete_tratado')
    BaseAlegrete = Alegrete [[
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

    CBom = pd.read_csv('Ambiente de teste-treinamento/RS_CBom_tratado')
    BaseCampoBom = CBom [[
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

    CaLe = pd.read_csv('Ambiente de teste-treinamento/RS_CaLe_tratado')
    BaseCapaoLeao = CaLe [[
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

    camaqua = pd.read_csv('Ambiente de teste-treinamento/RS_Camaqua_tratado')
    BaseCamaqua = camaqua [[
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

    Cangucu = pd.read_csv('Ambiente de teste-treinamento/RS_Cangucu_tratado')
    BaseCangucu = Cangucu [[
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

    Dom_Pedritoo = pd.read_csv('Ambiente de teste-treinamento/RS_Dom Pedrito_tratado')
    BaseDomPedrito = Dom_Pedritoo [[
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

    Jaguarao = pd.read_csv('Ambiente de teste-treinamento/RS_Jaguarão_tratado')
    BaseJaguarao = Jaguarao [[
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

    Mostardas = pd.read_csv('Ambiente de teste-treinamento/RS_Mostardas_tratado')
    BaseMostardas = Mostardas [[
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

    pAlegre = pd.read_csv('Ambiente de teste-treinamento/RS_PAlegre_tratado')
    BasePortoAlegre = pAlegre [[
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

    Sao_Gabriel = pd.read_csv('Ambiente de teste-treinamento/RS_São Gabriel_tratado')
    BaseSaoGabriel = Sao_Gabriel [[
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

    Uruguaiana = pd.read_csv('Ambiente de teste-treinamento/RS_Uruguaiana_tratado')
    BaseUruguaiana = Uruguaiana [[
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
    bases = [BaseAlegrete, BaseCampoBom, BaseCapaoLeao, BaseCamaqua, BaseCangucu, BaseDomPedrito, BaseJaguarao, BaseMostardas, BasePortoAlegre, BaseSaoGabriel, BaseUruguaiana]
    nomes_estacoes = ['Alegrete', 'Campo_Bom', 'Capao_Leao', 'Camaqua', 'Cangucu', 'Dom_Pedrito', 'Jaguarao', 'Mostardas', 'Porto_Alegre', 'Sao_Gabriel', 'Uruguaiana']

    # Atribuindo o nome da estação a cada DataFrame na lista 'bases'
    for df, nome in zip(bases, nomes_estacoes):
        df['Estação (RS)'] = nome

    # Concatenando todos os DataFrames em um único DataFrame
    BaseRS_Agrupado = pd.concat(bases, ignore_index=True)
    colunas = ['Estação (RS)'] + [col for col in BaseRS_Agrupado.columns if col != 'Estação (RS)']
    BaseRS_Agrupado = BaseRS_Agrupado[colunas]


    ## Transformando a BaseRS_Agrupada
    BaseRS_Agrupado = BaseRS_Agrupado.drop(columns=['Dia'])
    BaseRS_Agrupado = BaseRS_Agrupado.drop(columns=['Estação (RS)'])

    print(BaseRS_Agrupado ['Risco alagamento'].value_counts())
    print(BaseRS_Agrupado ['Altitude'].value_counts())
    altitude_map = {'Baixa': 1, 'Média': 2, 'Alta': 3}
    risco_alagamento_map = {'Sem Risco': 0, 'Risco Baixo': 1, 'Risco Moderado': 2, 'Risco Elevado': 3, 'Risco Crítico': 4}
    problemas_drenagem_map = {'Não': 0, 'Sim': 1}

    # Aplicando os mapeamentos nas colunas do DataFrame
    BaseRS_Agrupado['Altitude'] = BaseRS_Agrupado['Altitude'].map(altitude_map)
    BaseRS_Agrupado['Risco alagamento'] = BaseRS_Agrupado['Risco alagamento'].map(risco_alagamento_map)
    BaseRS_Agrupado['Problemas de Drenagem'] = BaseRS_Agrupado['Problemas de Drenagem'].map(problemas_drenagem_map)


    x_RS = BaseRS_Agrupado.values # Dados todos em formato de matriz (Criando base temporária)


    RS_cols = list(BaseRS_Agrupado.columns)
    RS_cols = [col for col in RS_cols if not any(keyword in col for keyword in ['Pressão', 'Temp', 'Umidade'])]
    RS_cols = [col for col in RS_cols if not col.startswith('Risco alagamento')]

    X_RS = BaseRS_Agrupado[RS_cols]
    y_RS = BaseRS_Agrupado[[col for col in BaseRS_Agrupado.columns if col.startswith('Risco alagamento')]]

    return X_RS, y_RS


def get_variaveis_PR2023():

        ## Criando DataFrames que serão Agrupados (PR)
    Colombo = pd.read_csv('Ambiente de teste-treinamento/PR_Colombo_tratado')
    BaseColombo = Colombo [[
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

    Curitiba = pd.read_csv('Ambiente de teste-treinamento/PR_Curitiba_tratado')
    BaseCuritiba = Curitiba [[
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

    Dois_Vizinhos = pd.read_csv('Ambiente de teste-treinamento/PR_Dois Vizinhos_tratado')
    BaseDois_Vizinhos = Dois_Vizinhos [[
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

    General_carneiro = pd.read_csv('Ambiente de teste-treinamento/PR_General Carneiro_tratado')
    BaseGeneral_Carneiro = General_carneiro [[
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

    Goiania = pd.read_csv('Ambiente de teste-treinamento/PR_Goiânia_tratado')
    BaseGoiania = Goiania [[
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

    Icaraima = pd.read_csv('Ambiente de teste-treinamento/PR_Icaraima_tratado')
    BaseIcaraima = Icaraima [[
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

    Joao_Tavares = pd.read_csv('Ambiente de teste-treinamento/PR_João_Tavares_tratado')
    BaseJoao_Tavares = Joao_Tavares [[
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

    Maringa = pd.read_csv('Ambiente de teste-treinamento/PR_Maringá_tratado')
    BaseMaringa = Maringa [[
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

    Morretes = pd.read_csv('Ambiente de teste-treinamento/PR_Morro_tratado')
    BaseMorretes = Morretes [[
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

    Sao_Matheus = pd.read_csv('Ambiente de teste-treinamento/PR_São Mateus do Sul_tratado')
    BaseSao_Matheus = Sao_Matheus [[
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
    bases = [BaseColombo, BaseCuritiba, BaseDois_Vizinhos, BaseGeneral_Carneiro, BaseGoiania, BaseIcaraima, BaseJoao_Tavares, BaseMaringa, BaseMorretes, BaseSao_Matheus]
    nomes_estacoes = ['Colombo', 'Curitiba', 'Dois_Vizinhos', 'General_Carneiro', 'Goiania', 'Icaraima', 'Joao_Tavares', 'Maringa', 'Morretes', 'Sao_Matheus']

    # Atribuindo o nome da estação a cada DataFrame na lista 'bases'
    for df, nome in zip(bases, nomes_estacoes):
        df['Estação (PR)'] = nome

    # Concatenando todos os DataFrames em um único DataFrame
    BasePR_Agrupado = pd.concat(bases, ignore_index=True)

    colunas = ['Estação (PR)'] + [col for col in BasePR_Agrupado.columns if col != 'Estação (PR)']
    BasePR_Agrupado = BasePR_Agrupado[colunas]


    ## Transformando a BasePR_Agrupada

    BasePR_Agrupado = BasePR_Agrupado.drop(columns=['Dia'])
    BasePR_Agrupado = BasePR_Agrupado.drop(columns=['Estação (PR)'])


    altitude_map = {'Baixa': 1, 'Média': 2, 'Alta': 3}
    risco_alagamento_map = {'Sem Risco': 0, 'Risco Baixo': 1, 'Risco Moderado': 2, 'Risco Elevado': 3, 'Risco Crítico': 4}
    problemas_drenagem_map = {'Não': 0, 'Sim': 1}

    # Aplicando os mapeamentos nas colunas do DataFrame
    BasePR_Agrupado['Altitude'] = BasePR_Agrupado['Altitude'].map(altitude_map)
    BasePR_Agrupado['Risco alagamento'] = BasePR_Agrupado['Risco alagamento'].map(risco_alagamento_map)
    BasePR_Agrupado['Problemas de Drenagem'] = BasePR_Agrupado['Problemas de Drenagem'].map(problemas_drenagem_map)


    x_PR = BasePR_Agrupado.values # Dados todos em formato de matriz (Criando base temporária)

    PR_cols = list(BasePR_Agrupado.columns)
    PR_cols = [col for col in PR_cols if not any(keyword in col for keyword in ['Pressão', 'Temp', 'Umidade'])]
    PR_cols = [col for col in PR_cols if not col.startswith('Risco alagamento')]
    X_PR = BasePR_Agrupado[PR_cols]
    y_PR = BasePR_Agrupado[[col for col in BasePR_Agrupado.columns if col.startswith('Risco alagamento')]]

    return X_PR, y_PR















