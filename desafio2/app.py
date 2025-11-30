import sqlite3
import os
from datetime import datetime

DB_PATH = os.getenv('DB_PATH', '/app/dados/banco.db')

def criar_e_popular():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mensagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT,
            timestamp TEXT
        )
    ''')
    
    mensagens = [
        "Primeira mensagem",
        "Volume Docker",
        "SQLite é legal",
        "Este dado sobrevive"
    ]
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for msg in mensagens:
        cursor.execute('INSERT INTO mensagens (texto, timestamp) VALUES (?, ?)', (msg, timestamp))
    
    conn.commit()
    conn.close()
    print(f" {len(mensagens)} mensagens gravadas!")

def ler_dados():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, texto, timestamp FROM mensagens')
    mensagens = cursor.fetchall()
    conn.close()
    
    print(f"Total: {len(mensagens)} mensagens")
    
    for id, texto, timestamp in mensagens:
        print(f"[{id}] {texto} - {timestamp}")

if __name__ == "__main__":
    print(f"SQLite Container | Banco: {DB_PATH}\n")
    
    # Se banco não existe, cria e popula
    if not os.path.exists(DB_PATH):
        print("Criando banco e inserindo dados...")
        criar_e_popular()
    
    print("\nLendo dados:")
    ler_dados()
