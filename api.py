from fastapi import FastAPI
from pydantic import BaseModel
import math

from database import criar_tabela, salvar_simulacao

criar_tabela()

app = FastAPI()

class SeguroInput(BaseModel):
    idade: int
    capital: float
    tipo: str


def calcular_premio(idade, capital, tipo):
    fatores = {
        "acidental": 0.0002,
        "natural": 0.0006
    }

    if tipo not in fatores:
        return None

    f = fatores[tipo]
    k = 0.035
    margem = 0.30

    risco_idade = math.exp(k * (idade - 18))
    premio = capital * f * risco_idade * (1 + margem)

    return round(premio, 2)


@app.post("/calcular")
def calcular(seguro: SeguroInput):
    premio = calcular_premio(
        seguro.idade,
        seguro.capital,
        seguro.tipo
    )

    salvar_simulacao(
    seguro.idade,
    seguro.capital,
    seguro.tipo,
    premio
)

    return {
        "idade": seguro.idade,
        "capital": seguro.capital,
        "tipo": seguro.tipo,
        "premio": premio
    }