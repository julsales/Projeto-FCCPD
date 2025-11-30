from flask import Flask, jsonify

app = Flask(__name__)

pedidos = [
    {"id": 1, "user_id": 1, "produto": "Notebook", "valor": 2500.00, "status": "Entregue"},
    {"id": 2, "user_id": 1, "produto": "Mouse", "valor": 50.00, "status": "Pendente"},
    {"id": 3, "user_id": 2, "produto": "Teclado", "valor": 150.00, "status": "Enviado"},
    {"id": 4, "user_id": 3, "produto": "Monitor", "valor": 800.00, "status": "Entregue"}
]

@app.route('/orders')
def listar_pedidos():
    return jsonify(pedidos)

@app.route('/orders/<int:id>')
def obter_pedido(id):
    pedido = next((p for p in pedidos if p['id'] == id), None)
    if pedido:
        return jsonify(pedido)
    return jsonify({"erro": "Pedido não encontrado"}), 404

@app.route('/orders/user/<int:user_id>')
def pedidos_usuario(user_id):
    pedidos_user = [p for p in pedidos if p['user_id'] == user_id]
    return jsonify(pedidos_user)

if __name__ == '__main__':
    print("Orders Service iniciado na porta 8002")
    app.run(host='0.0.0.0', port=8002)
