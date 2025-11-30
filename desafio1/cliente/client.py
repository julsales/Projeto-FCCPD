import requests
import time
import logging
import os

SERVIDOR_URL = "http://servidor-web:8080"
INTERVALO = 5

# Logs
os.makedirs('/app/logs', exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/app/logs/cliente.log'),
        logging.StreamHandler()
    ]
)

def fazer_requisicao():
    try:
        response = requests.get(SERVIDOR_URL, timeout=10)
        dados = response.json()
        logging.info(f"Requisição #{dados.get('requisicoes_recebidas')} - {dados.get('mensagem')}")
    except requests.exceptions.ConnectionError:
        logging.error(" Servidor inacessível")
    except requests.exceptions.Timeout:
        logging.error("Timeout na conexão")
    except Exception as e:
        logging.error(f" Erro: {e}")

if __name__ == "__main__":
    logging.info(f"Requisições a cada {INTERVALO}s")
    
    while True:
        fazer_requisicao()
        time.sleep(INTERVALO)

