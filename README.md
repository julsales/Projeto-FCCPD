# Projeto FCCPD - Fundamentos de Computação em Nuvem e Processamento Distribuído

[![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.11-green?logo=python)](https://www.python.org/)

## 📖 Sobre o Projeto

Este repositório contém as soluções desenvolvidas para os desafios práticos da disciplina de Fundamentos de Computação em Nuvem e Processamento Distribuído (FCCPD). O objetivo é demonstrar conhecimentos em containerização, orquestração, microsserviços e arquiteturas distribuídas.

## 🎯 Desafios

### Desafios com Docker

| Desafio | Status | Descrição |
|---------|--------|-----------|
| [**Desafio 1**](./desafio1/) | ✅ Completo | Containers em Rede - Comunicação entre containers via rede Docker customizada |
| [**Desafio 2**](./desafio2/) | 🚧 Em breve | A ser definido |
| [**Desafio 3**](./desafio3/) | 🚧 Em breve | A ser definido |

### Outros Desafios

| Desafio | Status | Descrição |
|---------|--------|-----------|
| [**Desafio 4**](./desafio4/) | 🚧 Em breve | A ser definido |
| [**Desafio 5**](./desafio5/) | 🚧 Em breve | A ser definido |

---

### ✅ Desafio 1 — Containers em Rede

**Status**: ✅ Concluído

**Objetivo**: Criar dois containers que se comunicam por uma rede Docker customizada.

**Tecnologias**: Docker, Python, Flask, Docker Compose

**Características**:
- ✓ Servidor web Flask na porta 8080
- ✓ Cliente HTTP fazendo requisições periódicas
- ✓ Rede Docker customizada (`rede-desafio`)
- ✓ Logs detalhados de comunicação
- ✓ Scripts de automação para Windows e Linux

[📖 Ver documentação completa do Desafio 1](./desafio1/README.md)

---

## 📁 Estrutura do Repositório

```
Projeto-FCCPD/
│
├── desafio1/                    # Desafio 1 - Containers em Rede
│   ├── servidor/
│   │   ├── Dockerfile
│   │   ├── app.py
│   │   └── requirements.txt
│   ├── cliente/
│   │   ├── Dockerfile
│   │   ├── client.py
│   │   └── requirements.txt
│   ├── docker-compose.yml
│   ├── iniciar.ps1
│   ├── parar.ps1
│   ├── ARQUITETURA.md
│   ├── EXEMPLOS.md
│   ├── TESTES.md
│   └── README.md
│
├── desafio2/                    # Desafio 2 - Em breve
│   └── README.md
│
├── desafio3/                    # Desafio 3 - Em breve
│   └── README.md
│
├── desafio4/                    # Desafio 4 - Em breve
│   └── README.md
│
├── desafio5/                    # Desafio 5 - Em breve
│   └── README.md
│
├── .gitignore
└── README.md                    # Este arquivo
```

## 🚀 Como Usar

Cada desafio possui sua própria pasta com documentação detalhada. Para executar um desafio específico:

1. Navegue até a pasta do desafio desejado
2. Leia o README.md específico do desafio
3. Execute os scripts de inicialização fornecidos

**Exemplo para o Desafio 1**:
```powershell
cd desafio1
.\iniciar.ps1
```

### Navegação Rápida

- [Desafio 1 - Containers em Rede](./desafio1/README.md) ✅
- [Desafio 2](./desafio2/README.md) 🚧
- [Desafio 3](./desafio3/README.md) 🚧
- [Desafio 4](./desafio4/README.md) 🚧
- [Desafio 5](./desafio5/README.md) 🚧

## 🛠️ Tecnologias Utilizadas

- **Docker** - Containerização de aplicações
- **Docker Compose** - Orquestração de múltiplos containers
- **Python 3.11** - Linguagem de programação
- **Flask** - Framework web para o servidor
- **Requests** - Biblioteca HTTP para o cliente

## 📋 Pré-requisitos

Para executar os projetos deste repositório, você precisará ter instalado:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (inclui Docker e Docker Compose)
- Git (para clonar o repositório)

## 🎓 Objetivos de Aprendizado

Este projeto visa desenvolver competências em:

- ✅ Containerização de aplicações com Docker
- ✅ Configuração de redes Docker customizadas
- ✅ Comunicação entre containers
- ✅ Orquestração com Docker Compose
- ✅ Desenvolvimento de aplicações distribuídas
- ✅ Logging e monitoramento de containers
- ✅ Boas práticas de DevOps

## ⚠️ Importante

- ✅ Este projeto foi desenvolvido de forma **autoral e original**
- ✅ Todo o código está **documentado e explicado** nos READMEs
- ✅ Ferramentas de IA foram usadas apenas como **apoio**, não como gerador completo
- ✅ O desenvolvedor **compreende e pode explicar** toda a solução

## 📞 Contato

Para dúvidas ou sugestões sobre este projeto, entre em contato através do GitHub.

## 📄 Licença

Este projeto é de código aberto e está disponível para fins educacionais.

---

**Última atualização**: 28 de Novembro de 2025
