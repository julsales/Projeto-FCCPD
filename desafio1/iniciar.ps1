# Windows (PowerShell)

Write-Host "[1/4] Parando containers existentes..." -ForegroundColor Yellow
docker-compose down 2>$null

Write-Host ""
Write-Host "[2/4] Criando rede Docker customizada..." -ForegroundColor Yellow
docker network create rede-desafio --driver bridge --subnet 172.25.0.0/16 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Rede já existe, continuando..." -ForegroundColor Gray
}

Write-Host ""
Write-Host "[3/4] Construindo imagens Docker..." -ForegroundColor Yellow
docker-compose build

Write-Host ""
Write-Host "[4/4] Iniciando containers..." -ForegroundColor Yellow
docker-compose up -d

Write-Host ""
Write-Host "Servidor Web: " -NoNewline
Write-Host "http://localhost:8080" -ForegroundColor Cyan
Write-Host ""
Write-Host "Comandos úteis:" -ForegroundColor Yellow
Write-Host "  - Ver logs do servidor:  docker logs -f servidor-web"
Write-Host "  - Ver logs do cliente:   docker logs -f cliente-http"
Write-Host "  - Ver todos os logs:     docker-compose logs -f"
Write-Host "  - Parar os containers:   docker-compose down"
Write-Host ""
