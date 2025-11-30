# Desafio 3 — Docker Compose Orquestrando Serviços

## Descrição

Aplicação web demonstra orquestração de três serviços na rede bridge dependentes com Docker Compose. Flask comunica-se com PostgreSQL (banco) e Redis (cache).

## Funcionamento

Endpoint raiz (`/`) incrementa contador Redis, insere registro no PostgreSQL e retorna número do visitante. Existe a comunicação simultânea entre os três serviços.

## Decisões Técnicas

Sleep de 10 segundos garante serviços prontos. Redis para contador rápido em memória, PostgreSQL para histórico persistente com timestamps. Variáveis de ambiente evitam credenciais hardcoded. Rede bridge permite comunicação por nomes DNS (`postgres`, `redis`). Volume nomeado persiste dados do PostgreSQL.

## Como Executar

**Iniciar:**
```bash
docker-compose up --build
```

**Acessar:**
```
http://localhost:5000
```

**Parar:**
```bash
docker-compose down
```

## Exemplo de Saída

**Primeira visita:**
```
Visitante número: 1
```

**Segunda visita:**
```
Visitante número: 2
```

**Quinta visita:**
```
Visitante número: 5
```

Contador incrementa a cada acesso. PostgreSQL armazena histórico completo na tabela `historico`.

