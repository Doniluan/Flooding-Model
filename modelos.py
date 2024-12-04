import joblib

def carregar_modeloSP(caminho_modelo='SP_Flooding_Model.joblib'):
    modelo = joblib.load(caminho_modelo)
    print(f"Modelo carregado com sucesso: {caminho_modelo}")
    return modelo
        
def carregar_modeloRJ(caminho_modelo='RJ_Flooding_Model.joblib'):
    modelo = joblib.load(caminho_modelo)
    print(f"Modelo carregado com sucesso: {caminho_modelo}")
    return modelo  

def carregar_modeloMG(caminho_modelo='MG_Flooding_Model.joblib'):
    modelo = joblib.load(caminho_modelo)
    print(f"Modelo carregado com sucesso: {caminho_modelo}")
    return modelo

def carregar_modeloSC(caminho_modelo='SC_Flooding_Model.joblib'):
    modelo = joblib.load(caminho_modelo)
    print(f"Modelo carregado com sucesso: {caminho_modelo}")
    return modelo

def carregar_modeloRS(caminho_modelo='RS_Flooding_Model.joblib'):
    modelo = joblib.load(caminho_modelo)
    print(f"Modelo carregado com sucesso: {caminho_modelo}")
    return modelo

def carregar_modeloPR(caminho_modelo='PR_Flooding_Model.joblib'):
    modelo = joblib.load(caminho_modelo)
    print(f"Modelo carregado com sucesso: {caminho_modelo}")
    return modelo

