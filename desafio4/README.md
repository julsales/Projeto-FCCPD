# Desafio 4 — Microsserviços Independentes

## Descrição

Dois microsserviços independentes se comunicam via HTTP. Serviço A fornece lista de usuários (JSON), Serviço B consome A e enriquece dados mostrando tempo de atividade.

## Arquitetura

**Serviço A** (porta 8001): API REST que retorna lista de usuários com id, nome, email e data de cadastro. Funciona como fonte de dados.

**Serviço B** (porta 8002): Consome API do Serviço A via HTTP, calcula dias desde cadastro e retorna informações enriquecidas (status "Ativo há X dias").

Comunicação via requisições HTTP usando hostname DNS do Docker (servico-a:8001). Cada serviço tem Dockerfile isolado.

## Decisões Técnicas

Flask foi escolhido pela simplicidade em criar aplicações com APIs REST. Serviços isolados em containers separados com Dockerfiles independentes. Variável de ambiente `SERVICO_A_URL` permite configurar endpoint do Serviço A. Rede Docker bridge permite comunicação por nome. Depends_on garante que Serviço A inicie antes de B.

## Funcionamento

Serviço A mantém dados mockados de usuários em memória. Serviço B faz requisição GET para Serviço A, processa resposta calculando diferença de dias entre data de cadastro e data atual, e retorna JSON enriquecido.

## Como Executar

**Iniciar:**
```bash
cd desafio4
docker-compose up --build
```

**Testar Serviço A:**
```bash
curl http://localhost:8001/usuarios
```

**Testar Serviço B:**
```bash
curl http://localhost:8002/usuarios-ativos
```

**Parar:**
```bash
docker-compose down
```

## Endpoints

**Serviço A:**
- `GET /usuarios` - Lista todos usuários
- `GET /usuarios/<id>` - Busca usuário específico

**Serviço B:**
- `GET /` - Informações do serviço
- `GET /usuarios-ativos` - Usuários com tempo de atividade

## Exemplo de Saída

**Serviço A (GET /usuarios):**
```json
[
  {
    "data_cadastro": "2024-01-15",
    "email": "ana@email.com",
    "id": 1,
    "nome": "Ana Silva"
  },
  {
    "data_cadastro": "2024-03-20",
    "email": "carlos@email.com",
    "id": 2,
    "nome": "Carlos Santos"
  },
  {
    "data_cadastro": "2024-06-10",
    "email": "maria@email.com",
    "id": 3,
    "nome": "Maria Costa"
  }
]
```

**Serviço B (GET /usuarios-ativos):**
```json
{
  "total": 3,
  "usuarios": [
    {
      "cadastro": "2024-01-15",
      "email": "ana@email.com",
      "nome": "Ana Silva",
      "status": "Ativo há 685 dias"
    },
    {
      "cadastro": "2024-03-20",
      "email": "carlos@email.com",
      "nome": "Carlos Santos",
      "status": "Ativo há 620 dias"
    },
    {
      "cadastro": "2024-06-10",
      "email": "maria@email.com",
      "nome": "Maria Costa",
      "status": "Ativo há 538 dias"
    }
  ]
}
```

