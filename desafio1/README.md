# Desafio 1 — Containers em Rede

## 📋 Descrição da Solução

Este projeto implementa dois containers Docker que se comunicam através de uma rede customizada:

- **Servidor Web (Flask)**: API REST na porta 8080 que registra cada requisição recebida
- **Cliente HTTP**: Envia requisições automáticas ao servidor a cada 5 segundos

**Objetivo**: Demonstrar comunicação entre containers usando rede Docker customizada com DNS interno.

---

## 🏗️ Arquitetura

A arquitetura é baseada em uma **rede customizada** chamada `rede-desafio` que utiliza o driver bridge do Docker com subnet 172.25.0.0/16. Esta rede fornece um DNS interno que permite que os containers se comuniquem usando nomes ao invés de IPs fixos, facilitando a manutenção e escalabilidade.

O **container servidor** roda uma imagem Python 3.11 slim com o framework Flask 3.0.0. Ele expõe dois endpoints: o principal (`/`) que retorna informações sobre as requisições recebidas, e o `/status` usado para health checks do Docker. Todos os eventos são registrados em `/app/logs/servidor.log` para análise posterior.

Já o **container cliente** também utiliza Python 3.11 slim, mas com a biblioteca requests 2.31.0 para fazer chamadas HTTP. Ele funciona em loop contínuo enviando requisições ao servidor a cada 5 segundos, registrando as respostas em `/app/logs/cliente.log`. Essa comunicação constante demonstra na prática como containers isolados conseguem trocar dados através da rede Docker.

---

## 🔧 Decisões Técnicas

A escolha de **Python 3.11** foi motivada pela sua simplicidade, ampla adoção na comunidade e vasto ecossistema de bibliotecas maduras. Para o servidor web, optamos pelo **Flask** por ser um framework minimalista e ideal para construir APIs REST sem complexidade desnecessária. No lado do cliente, a biblioteca **Requests** é o padrão de mercado para comunicação HTTP em Python, oferecendo uma interface intuitiva e robusta.

A configuração de **rede Docker** utiliza o driver bridge para garantir isolamento entre containers no mesmo host. Definimos IPs fixos (172.25.0.10 para o servidor e 172.25.0.20 para o cliente) para facilitar o debugging e a identificação nos logs. O DNS automático do Docker permite que o cliente se comunique com o servidor usando apenas o nome `servidor-web`, sem necessidade de hardcoded IPs.

O sistema de **logging** implementa saída dupla: os logs aparecem tanto no console (acessível via `docker logs`) quanto em arquivos persistentes. Usamos volumes locais para mapear a pasta `./logs` do projeto, permitindo acesso fácil aos logs sem precisar entrar nos containers. O formato estruturado (timestamp - level - mensagem) facilita análise e debugging.

O **Docker Compose** foi escolhido para orquestração porque permite declarar toda a infraestrutura em um único arquivo YAML. Ele gerencia automaticamente as dependências entre serviços, garante a criação da rede customizada e implementa health checks para monitorar a disponibilidade do servidor.

---

## 🔍 Funcionamento Detalhado

### Fluxo de Comunicação

O processo começa com o **Docker Compose criando a rede** `rede-desafio` e inicializando os containers. O servidor-web recebe o IP 172.25.0.10 e fica aguardando requisições na porta 8080, enquanto o cliente-http obtém o IP 172.25.0.20 e se prepara para iniciar as chamadas HTTP.

A cada **5 segundos**, o cliente executa uma requisição GET para `http://servidor-web:8080`. Note que ele usa o nome `servidor-web` ao invés do IP, graças ao DNS interno do Docker. Quando o servidor recebe a requisição, ele incrementa um contador global, registra o evento no log (incluindo IP de origem e timestamp), e retorna um JSON com informações sobre o estado atual.

O **JSON de resposta** contém a mensagem "Servidor Flask funciona", o timestamp exato, o número total de requisições recebidas desde que o servidor iniciou, e o ID do container. Ao receber essa resposta, o cliente processa os dados, exibe no console, registra no arquivo de log, e aguarda mais 5 segundos antes de repetir o ciclo.

Este **loop contínuo** demonstra comunicação persistente entre containers: o servidor está sempre disponível respondendo requisições, enquanto o cliente atua como consumidor periódico da API. Todo esse fluxo é registrado em arquivos de log acessíveis na pasta local `./logs`, permitindo análise detalhada da comunicação mesmo após os containers serem parados.

---

## Como Executar

**1. Clonar o Repositório**
```bash
git clone https://github.com/julsales/Projeto-FCCPD.git
cd Projeto-FCCPD/desafio1
```

**2. Iniciar os Containers**

**Opção A - Usando script (Windows):**
```powershell
.\iniciar.ps1
```

**Opção B - Usando Docker Compose diretamente:**
```bash
# Construir as imagens e iniciar containers
docker-compose up -d --build

# Verificar se estão rodando
docker ps
```

**Saída esperada:**
```
CONTAINER ID   IMAGE                    STATUS         PORTS
abc123...      desafio1-servidor-web    Up 10 seconds  0.0.0.0:8080->8080/tcp
def456...      desafio1-cliente-http    Up 10 seconds
```

**3. Verificar Logs**

**Ver logs no terminal:**
```bash
# Logs do servidor
docker logs -f servidor-web

# Logs do cliente
docker logs -f cliente-http

# Ambos simultaneamente
docker-compose logs -f
```

**Ver logs nos arquivos (pasta local):**
```bash
# Windows
notepad logs\servidor.log
notepad logs\cliente.log

# Linux/Mac
cat logs/servidor.log
tail -f logs/cliente.log
```

**4. Testar a Comunicação**

**Navegador:**
- Acesse: http://localhost:8080
- Você verá um JSON com informações do servidor

**PowerShell:**
```powershell
Invoke-WebRequest -Uri http://localhost:8080 | ConvertFrom-Json
```

**Curl:**
```bash
curl http://localhost:8080
```

**Resposta esperada:**
```json
{
  "mensagem": "Servidor Flask funciona",
  "timestamp": "2025-11-29 21:30:15",
  "requisicoes_recebidas": 1,
  "container_id": "eac50d32fad7"
}
```

#### 5. Parar os Containers

```bash
docker-compose down
```
---

## 📊 Demonstração dos Logs

### Logs do Servidor (recebendo requisições)
```log
2025-11-29 21:30:05 - INFO - Servidor Flask iniciado na porta 8080
2025-11-29 21:30:10 - INFO - Requisição #1 recebida - IP: eac50d32fad7
2025-11-29 21:30:15 - INFO - Requisição #2 recebida - IP: eac50d32fad7
2025-11-29 21:30:20 - INFO - Requisição #3 recebida - IP: eac50d32fad7
```

### Logs do Cliente (enviando requisições)
```log
2025-11-29 21:30:05 - INFO - Cliente HTTP iniciado
2025-11-29 21:30:10 - INFO - --- Requisição #1 ---
2025-11-29 21:30:10 - INFO - Enviando requisição para http://servidor-web:8080
2025-11-29 21:30:10 - INFO - Resposta OK - Total de requisições: 1
2025-11-29 21:30:15 - INFO - --- Requisição #2 ---
2025-11-29 21:30:15 - INFO - Resposta OK - Total de requisições: 2
```

**Obs. dos logs:**
-  IP `172.25.0.20` (cliente) aparece nos logs do servidor
-  Timestamps sincronizados
-  Contador de requisições incrementando
-  Comunicação via nome DNS (`servidor-web`)

---
