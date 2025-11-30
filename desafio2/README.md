# Desafio 2 — Volumes e Persistência

## Descrição

Demonstra persistência de dados usando volumes Docker. Container escreve dados em banco SQLite que sobrevive mesmo após remoção do container.

## Funicionamento

Script Python detecta se banco existe: se não, cria e insere dados, se sim, apenas lê. SQLite com volume mapeado para `./dados` garante persistência fora do container.

## Decisões Técnicas

SQLite escolhido pela simplicidade (arquivo único). Volume Docker mapeia `./dados` do host para `/app/dados` no container. Lógica de verificação (`os.path.exists()`) evita duplicação e demonstra persistência claramente.

## Como Executar

**Iniciar:**
```bash
docker-compose up --build
```

**Provar persistência:**
```bash
docker-compose down
docker-compose up
```

Dados não são recriados na segunda execução, apenas lidos.

## Exemplo de Saída

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

**Segunda execução (após down):**
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

Note ausência de "Criando banco" na segunda vez.

