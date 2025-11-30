import os
from flask import Flask, jsonify
import requests

app = Flask(__name__)

USERS_URL = os.getenv('USERS_SERVICE_URL', 'http://localhost:8001')
ORDERS_URL = os.getenv('ORDERS_SERVICE_URL', 'http://localhost:8002')

@app.route('/')
def index():
    return jsonify({
        "gateway": "API Gateway",
        "endpoints": ["/users", "/orders", "/users/<id>", "/orders/<id>"]
    })

@app.route('/users')
def get_users():
    try:
        response = requests.get(f'{USERS_URL}/users')
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/users/<int:id>')
def get_user(id):
    try:
        response = requests.get(f'{USERS_URL}/users/{id}')
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/orders')
def get_orders():
    try:
        response = requests.get(f'{ORDERS_URL}/orders')
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/orders/<int:id>')
def get_order(id):
    try:
        response = requests.get(f'{ORDERS_URL}/orders/{id}')
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    print("API Gateway iniciado na porta 8000")
    print(f"Users Service: {USERS_URL}")
    print(f"Orders Service: {ORDERS_URL}")
    app.run(host='0.0.0.0', port=8000)
