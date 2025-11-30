# Desafio 1 — Containers em Rede

## Descrição

Dois containers Docker se comunicam através de rede Docker customizada. Servidor Flask (porta 8080) registra requisições recebidas, enquanto cliente HTTP envia requisições automáticas a cada 5 segundos.

## Arquitetura

Rede customizada **rede-desafio** (driver bridge, subnet 172.25.0.0/16) foi criada no docker-compose.yml. Conecta servidor (IP 172.25.0.10) rodando Flask 3.0.0 com endpoints `/` e `/status`, e cliente (IP 172.25.0.20) usando requests 2.31.0. DNS interno permite comunicação por nome ao invés de IP.

## Funcionamento

Docker Compose cria a rede e inicia containers. Cliente envia GET para `http://servidor-web:8080` a cada 5 segundos. Servidor incrementa contador, loga evento e retorna JSON com mensagem, timestamp, total de requisições e container ID. Cliente processa resposta e registra em log. Ciclo se repete continuamente.

## Decisões Técnicas

Python 3.11 foi escolhido pela simplicidade e bibliotecas maduras. Flask oferece API REST minimalista, enquanto requests é padrão para HTTP em Python. IPs fixos facilitam debugging. DNS automático permite comunicação por nome (`servidor-web`). Logging duplo (console + arquivo) com volumes locais para acesso fácil. Docker Compose gerencia infraestrutura e dependências.


## Como Executar

**Iniciar:**
```bash
cd desafio1
docker-compose up -d --build
```

**Ver logs:**
```bash
docker-compose logs -f
# ou acessar arquivos em ./logs/
```

**Testar:**
```bash
curl http://localhost:8080
```

**Parar:**
```bash
docker-compose down
```

## Exemplo de Logs

**Servidor:**
```
2025-11-29 21:30:05 - INFO - Servidor Flask iniciado na porta 8080
2025-11-29 21:30:10 - INFO - Requisição #1 recebida - IP: eac50d32fad7
2025-11-29 21:30:15 - INFO - Requisição #2 recebida - IP: eac50d32fad7
```

**Cliente:**
```
2025-11-29 21:30:05 - INFO - Cliente HTTP iniciado
2025-11-29 21:30:10 - INFO - --- Requisição #1 ---
2025-11-29 21:30:10 - INFO - Resposta OK - Total de requisições: 1
```
