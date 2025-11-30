from flask import Flask, jsonify
from datetime import datetime
import os
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Logs
log_dir = '/app/logs'
os.makedirs(log_dir, exist_ok=True)

file_handler = RotatingFileHandler(
    f'{log_dir}/servidor.log',
    maxBytes=10*1024*1024,  
    backupCount=5
)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'
))

app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)


cont_requisicoes = 0

@app.route('/')
def home():
    
    global cont_requisicoes
    cont_requisicoes = cont_requisicoes + 1
    
    resposta = {
        'mensagem': 'Servidor Flask funcionando',
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'requisicoes_recebidas': cont_requisicoes,
        'container_id': os.uname().nodename
    }
    
    log_msg = f"Requisição #{cont_requisicoes} recebida - IP: {resposta['container_id']}"
    print(f"[LOG] {log_msg}")
    app.logger.info(log_msg)  
    
    return jsonify(resposta), 200

@app.route('/status')
def status():
    # Status do servidor
    return jsonify({
        'status': 'online',
        'servidor': 'Flask Web Server',
        'porta': 8080
    }), 200

if __name__ == '__main__':
    print("=" * 50)
    print("Servidor Flask iniciado na porta 8080")
    print(f"Logs salvos em: {log_dir}/servidor.log")
    print("=" * 50)
    app.logger.info("Servidor Flask iniciado na porta 8080")
    app.run(host='0.0.0.0', port=8080, debug=False)
