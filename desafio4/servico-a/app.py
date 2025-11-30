from flask import Flask, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "Ana Silva", "email": "ana@email.com", "data_cadastro": "2024-01-15"},
    {"id": 2, "nome": "Carlos Santos", "email": "carlos@email.com", "data_cadastro": "2024-03-20"},
    {"id": 3, "nome": "Maria Costa", "email": "maria@email.com", "data_cadastro": "2024-06-10"}
]

@app.route('/usuarios')
def listar_usuarios():
    return jsonify(usuarios)

@app.route('/usuarios/<int:id>')
def obter_usuario(id):
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if usuario:
        return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado"}), 404

if __name__ == '__main__':
    print("Microsserviço A iniciado - Lista de usuários")
    app.run(host='0.0.0.0', port=8001)
