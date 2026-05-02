# 🛡️ Aegis Vita — Simulador de Seguro de Vida

![Aegis Vita Banner](./banner.png)

Projeto desenvolvido para simulação de prêmios de seguro de vida com base em **idade**, **capital segurado** e **tipo de cobertura**, utilizando um modelo de risco com crescimento exponencial.

---

## 🎯 Objetivo

Simular o cálculo de prêmios de seguros de vida, permitindo a análise do comportamento do custo ao longo do tempo e apoio na tomada de decisão financeira.

---

## ⚙️ Funcionalidades

✔ Simulação de prêmio (morte natural e acidental)  
✔ API REST com FastAPI  
✔ Persistência de dados com SQLite  
✔ Geração de gráficos com Matplotlib  
✔ Exportação de dados para Excel  

---

## 🧠 Regra de Negócio

O cálculo do prêmio considera:

- Idade do cliente  
- Capital segurado  
- Tipo de cobertura  
- Crescimento exponencial do risco com a idade  

📌 Fórmula aplicada:

```
premio = capital × fator × e^(k × (idade - 18)) × (1 + margem)
```

---

## 🛠️ Tecnologias

- Python  
- FastAPI  
- Pandas  
- Matplotlib  
- SQLite  

---

## 🚀 Como executar o projeto

```bash
pip install -r requirements.txt
uvicorn api:app --reload
```

Acesse a documentação automática em:

👉 http://127.0.0.1:8000/docs

---

## 🌐 Endpoint da API

### POST `/calcular`

### Exemplo de requisição:

```json
{
  "idade": 55,
  "capital": 180000,
  "tipo": "natural"
}
```

### Resposta:

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

- O prêmio cresce exponencialmente com a idade  
- Cobertura natural possui maior custo que acidental  
- O capital segurado impacta diretamente o valor final  

---

## 📁 Estrutura do projeto

```
api.py        # API FastAPI
main.py       # Simulação e gráficos
database.py   # Persistência SQLite
```

---

## 👩‍💻 Autora

**Caroline Cunha**  
Especialista em Investimentos | Inteligência de Mercado | Seguros de Vida  
Em transição para Data Analytics

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
```

---

## 👩‍💻 Autora

Caroline Cunha
Especialista em Investimentos | Inteligência de Mercado | Seguros de Vida
Em transição para Data Analytics
