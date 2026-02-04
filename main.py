from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# ESSENCIAL: Configuração de CORS para o Vue conseguir acessar o Python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite que o Frontend acesse a API
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/operadoras")
def listar_operadoras(page: int = 1, limit: int = 10):
    try:
        # Carrega o CSV (certifique-se que o arquivo está na mesma pasta)
        df = pd.read_csv("consolidado_despesas.csv")
        
        total = len(df)
        inicio = (page - 1) * limit
        fim = inicio + limit

        # Seleciona o pedaço dos dados (paginação)
        dados = df.iloc[inicio:fim].to_dict(orient="records")

        return {
            "dados": dados,
            "total": total,
            "page": page,
            "limit": limit
        }
    except Exception as e:
        return {"error": str(e), "dados": [], "total": 0}