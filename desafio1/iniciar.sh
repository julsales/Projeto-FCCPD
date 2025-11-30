#!/bin/bash

echo "[1/4] Parando containers existentes..."
docker-compose down 2>/dev/null

echo ""
echo "[2/4] Criando rede Docker customizada..."
docker network create rede-desafio --driver bridge --subnet 172.25.0.0/16 2>/dev/null || echo "Rede já existe, continuando..."

echo ""
echo "[3/4] Construindo imagens Docker..."
docker-compose build

echo ""
echo "[4/4] Iniciando containers..."
docker-compose up -d


echo ""
echo "Servidor Web: http://localhost:8080"
echo ""
echo "Comandos úteis:"
echo "  - Ver logs do servidor:  docker logs -f servidor-web"
echo "  - Ver logs do cliente:   docker logs -f cliente-http"
echo "  - Ver todos os logs:     docker-compose logs -f"
echo "  - Parar os containers:   docker-compose down"
echo ""
