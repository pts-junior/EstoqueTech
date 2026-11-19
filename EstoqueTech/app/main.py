from fastapi import FastAPI

app = FastAPI(
    title="EstoqueTech API",
    description="API para gerenciamento de ativos de TI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Bem-Vindo ao EstoqueTech!",
        "status": "online",
        "version": "1.0.0"
    }

@app.get("/health")
def health_chech():
    return {
        "status": "healtly"
    }

