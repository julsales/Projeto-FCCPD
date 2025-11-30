# Desafio 5 — Microsserviços com API Gateway

## Descrição

Arquitetura com API Gateway centralizando acesso a dois microsserviços. Gateway expõe endpoints `/users` e `/orders`, orquestrando chamadas aos serviços internos.

## Arquitetura

**API Gateway** (porta 8000): Ponto único de entrada. Recebe requisições externas e roteia para serviços apropriados. Não possui lógica de negócio, apenas encaminha requests.

**Users Service** (interno): Gerencia dados de usuários. Acessível apenas via gateway na rede interna.

**Orders Service** (interno): Gerencia pedidos. Também acessível apenas via gateway.

Cliente externo → Gateway (8000) → Users/Orders Services (rede interna)

## Decisões Técnicas

Gateway implementado com Flask fazendo proxy HTTP para serviços internos. Variáveis de ambiente configuram URLs dos serviços. Apenas gateway expõe porta ao host (8000), serviços internos ficam isolados na rede Docker. Depends_on garante que serviços iniciem antes do gateway.

## Funcionamento

Gateway recebe requisição HTTP, identifica rota (/users ou /orders), faz requisição ao serviço correspondente usando hostname DNS interno, e retorna resposta ao cliente. Serviços não são acessíveis diretamente do host.

## Como Executar

**Iniciar:**
```bash
cd desafio5
docker-compose up --build
```

**Testar via Gateway:**
```bash
curl http://localhost:8000/users
curl http://localhost:8000/orders
curl http://localhost:8000/users/1
curl http://localhost:8000/orders/1
```

**Parar:**
```bash
docker-compose down
```

## Endpoints

**Gateway (porta 8000):**
- `GET /` - Informações do gateway
- `GET /users` - Lista usuários (proxy para users-service)
- `GET /users/<id>` - Busca usuário (proxy)
- `GET /orders` - Lista pedidos (proxy para orders-service)
- `GET /orders/<id>` - Busca pedido (proxy)

## Exemplo de Saída

**GET /users:**
```json
[
  {
    "id": 1,
    "nome": "Ana Silva",
    "email": "ana@email.com",
    "cidade": "São Paulo"
  },
  {
    "id": 2,
    "nome": "Carlos Santos",
    "email": "carlos@email.com",
    "cidade": "Rio de Janeiro"
  },
  {"id": 3,
  "nome": "Maria Costa",
  "email": "maria@email.com",
  "cidade": "Brasília"
  }
]
```

**GET /orders:**
```json
[
  {
    "id": 1,
    "user_id": 1,
    "produto": "Notebook",
    "valor": 2500.0,
    "status": "Entregue"
  },
  {
    "id": 2,
    "user_id": 1,
    "produto": "Mouse",
    "valor": 50.0,
    "status": "Pendente"
  },
  {"id": 3, 
  "user_id": 2, 
  "produto": "Teclado", 
  "valor": 150.00, 
  "status": "Enviado"
  },
  {"id": 4,
  "user_id": 3,
  "produto": "Monitor",
  "valor": 800.00,
  "status": "Entregue"}
]
```
