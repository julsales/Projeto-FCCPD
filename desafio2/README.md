# Desafio 2 — Volumes e Persistência

## Descrição

Demonstra persistência de dados usando volumes Docker. Um container escreve dados em banco SQLite e outro lê, provando que os dados persistem mesmo após remoção dos containers.

## Solução

Um único script Python que detecta se o banco já existe: se não, cria e insere dados; se sim, apenas lê. Usamos SQLite (arquivo único) com volume Docker mapeado para `./dados`.

A persistência é garantida porque `banco.db` fica na pasta local do host. Ao remover o container e executar novamente, o script detecta que o banco já existe e pula a criação, provando que os dados persistiram.

## Como Executar

**1. Primeira execução (cria banco e insere dados):**
```bash
docker-compose up --build
```

**2. Verificar que dados foram salvos localmente:**
```bash
ls dados/               
```

**3. Provar persistência (remover container e executar novamente):**
```bash
docker-compose down
docker-compose up
```

Os dados **não serão recriados** se o banco já existe, apenas lidos.

## Resultados

**Saída da Primeira execução (cria dados):**
```
sqlite-container  | SQLite Container | Banco: /app/dados/banco.db

sqlite-container  | Criando banco e inserindo dados...                                          
sqlite-container  |  4 mensagens gravadas!      
sqlite-container  |                             
sqlite-container  | Lendo dados:                
sqlite-container  | Total: 4 mensagens          
sqlite-container  | [1] Primeira mensagem - 2025-11-30 04:33:43                                 
sqlite-container  | [2] Volume Docker - 2025-11-30 04:33:43                                     
sqlite-container  | [3] SQLite é legal - 2025-11-30 04:33:43                                    
sqlite-container  | [4] Este dado sobrevive - 2025-11-30 04:33:43        
```

**Saída da Segunda execução após `docker-compose down` (lê dados persistentes):**
```
sqlite-container  | SQLite Container | Banco: /app/dados/banco.db
sqlite-container  | 
sqlite-container  |                             
sqlite-container  | Lendo dados:                
sqlite-container  | Total: 4 mensagens          
sqlite-container  | [1] Primeira mensagem - 2025-11-30 04:33:43                                 
sqlite-container  | [2] Volume Docker - 2025-11-30 04:33:43                                     
sqlite-container  | [3] SQLite é legal - 2025-11-30 04:33:43                                    
sqlite-container  | [4] Este dado sobrevive - 2025-11-30 04:33:43                  
```

Note que **não aparece "Criando banco"** na segunda vez, provando que o banco persistiu.

## Decisões Técnicas

Escolhi o **SQLite** porque é mais simples que PostgreSQL: um único arquivo facilita visualização da persistência. O script detecta se o banco existe usando `os.path.exists()`, evitando duplicação de dados.

O volume Docker mapeia `./dados` do host para `/app/dados` no container, tornando o banco acessível e persistente. A lógica de "criar se não existe, senão apenas ler" demonstra claramente a persistência entre execuções.

