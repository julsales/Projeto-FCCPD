import os
from flask import Flask, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

SERVICO_A_URL = os.getenv('SERVICO_A_URL', 'http://localhost:8001')

@app.route('/')
def index():
    return jsonify({
        "servico": "Microsserviço B",
        "endpoints": ["/usuarios-ativos"]
    })

@app.route('/usuarios-ativos')
def usuarios_ativos():
    try:
        response = requests.get(f'{SERVICO_A_URL}/usuarios')
        usuarios = response.json()
        
        resultado = []
        for user in usuarios:
            data_cadastro = datetime.strptime(user['data_cadastro'], '%Y-%m-%d')
            dias_ativo = (datetime.now() - data_cadastro).days
            
            resultado.append({
                "nome": user['nome'],
                "email": user['email'],
                "status": f"Ativo há {dias_ativo} dias",
                "cadastro": user['data_cadastro']
            })
        
        return jsonify({
            "total": len(resultado),
            "usuarios": resultado
        })
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    print(f"Microsserviço B iniciado - Consulta Serviço A em {SERVICO_A_URL}")
    app.run(host='0.0.0.0', port=8002)
