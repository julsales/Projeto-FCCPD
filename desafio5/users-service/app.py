from flask import Flask, jsonify

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "Ana Silva", "email": "ana@email.com", "cidade": "São Paulo"},
    {"id": 2, "nome": "Carlos Santos", "email": "carlos@email.com", "cidade": "Rio de Janeiro"},
    {"id": 3, "nome": "Maria Costa", "email": "maria@email.com", "cidade": "Brasília"}
]

@app.route('/users')
def listar_usuarios():
    return jsonify(usuarios)

@app.route('/users/<int:id>')
def obter_usuario(id):
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if usuario:
        return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado"}), 404

if __name__ == '__main__':
    print("Users Service iniciado na porta 8001")
    app.run(host='0.0.0.0', port=8001)
