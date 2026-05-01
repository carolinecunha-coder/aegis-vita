# aegis-vita
# 🛡️ Aegis Vita - Simulador de Seguro de Vida

Projeto desenvolvido para simulação de prêmios de seguro com base em idade, capital segurado e tipo de cobertura.

---

## 🎯 Objetivo

Simular o cálculo de prêmios de seguros de vida, permitindo análise de risco e comportamento do custo ao longo da idade.

---

## ⚙️ Funcionalidades

* ✔ Simulação de prêmio (morte natural e acidental)
* ✔ API com FastAPI
* ✔ Persistência de dados com SQLite
* ✔ Geração de gráficos com Matplotlib
* ✔ Exportação para Excel

---

## 🧠 Regra de Negócio

O cálculo do prêmio considera:

* Idade do cliente
* Capital segurado
* Tipo de cobertura
* Crescimento exponencial do risco com a idade

---

## 🛠️ Tecnologias

* Python
* FastAPI
* Pandas
* Matplotlib
* SQLite

---

## 🚀 Como executar o projeto

```bash
pip install -r requirements.txt
uvicorn api:app --reload
```

---

## 🌐 Endpoint da API

### POST /calcular

Exemplo de requisição:

```json
{
  "idade": 55,
  "capital": 180000,
  "tipo": "natural"
}
```

Resposta:

```json
{
  "idade": 55,
  "capital": 180000,
  "tipo": "natural",
  "premio": 512.6
}
```

---

## 📊 Insights

* O prêmio cresce exponencialmente com a idade
* Cobertura natural possui maior custo que acidental
* O capital segurado impacta diretamente o valor final

---

## 📁 Estrutura do projeto

```
api.py
main.py
database.py
aegis_vita.db
```

---

## 👩‍💻 Autora

Caroline Cunha
Especialista em Investimentos | Inteligência de Mercado | Seguros de Vida
Em transição para Data Analytics
