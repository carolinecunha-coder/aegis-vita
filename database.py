import sqlite3

def conectar():
    return sqlite3.connect("aegis_vita.db")


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS simulacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        idade INTEGER,
        capital REAL,
        tipo TEXT,
        premio REAL
    )
    """)

    conn.commit()
    conn.close()


def salvar_simulacao(idade, capital, tipo, premio):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO simulacoes (idade, capital, tipo, premio)
    VALUES (?, ?, ?, ?)
    """, (idade, capital, tipo, premio))

    conn.commit()
    conn.close()