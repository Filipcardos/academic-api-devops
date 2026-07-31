
from fastapi import FastAPI

app = FastAPI(title="Academic API DevOps")

@app.get('/')
def home():
    return {'message':'Academic API DevOps'}

@app.get('/health')
def health():
    return {'status':'ok'}

@app.post('/media')
def calcular_media(nota1: float, nota2: float, nota3: float):
    media = round((nota1+nota2+nota3)/3,2)
    return {
        'media': media,
        'situacao': 'Aprovado' if media >= 7 else 'Reprovado'
    }
