# 🚀 Início Rápido - Projeto FCCPD

## ⚡ Começando em 3 Passos

### 1️⃣ Clone o Repositório
```bash
git clone https://github.com/julsales/Projeto-FCCPD.git
cd Projeto-FCCPD
```

### 2️⃣ Navegue até o Desafio
```bash
cd desafio1
```

### 3️⃣ Execute o Projeto
**Windows (PowerShell):**
```powershell
.\iniciar.ps1
```

**Linux/Mac (Bash):**
```bash
chmod +x iniciar.sh
./iniciar.sh
```

## ✅ Verificar se Funcionou

1. **Abra seu navegador**: http://localhost:8080
   - Você deve ver uma resposta JSON do servidor

2. **Veja os logs**:
   ```powershell
   # Logs do servidor
   docker logs -f servidor-web
   
   # Logs do cliente
   docker logs -f cliente-http
   ```

## 🛑 Parar o Projeto

**Windows:**
```powershell
.\parar.ps1
```

**Linux/Mac:**
```bash
./parar.sh
```

## 📚 Documentação Completa

Para mais detalhes, consulte:
- [README Principal](./README.md)
- [Desafio 1 - Documentação Completa](./desafio1/README.md)
- [Arquitetura Visual](./desafio1/ARQUITETURA.md)
- [Exemplos Práticos](./desafio1/EXEMPLOS.md)
- [Guia de Testes](./desafio1/TESTES.md)

## ❓ Problemas Comuns

**"Porta 8080 já está em uso"**
- Pare o serviço usando a porta ou mude para 8081 no docker-compose.yml

**"Docker não encontrado"**
- Instale o Docker Desktop: https://www.docker.com/products/docker-desktop/

**"Permissão negada" (Linux/Mac)**
- Execute: `chmod +x iniciar.sh`

## 💡 Dica

Use `docker-compose logs -f` para ver os logs de ambos os containers simultaneamente!

---

Bons estudos! 🎓
