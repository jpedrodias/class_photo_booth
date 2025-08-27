#!/bin/bash

# Script para iniciar o Docker Compose com o UID/GID correto
# Usar: chmod +x ./start.sh && ./start.sh

echo "=== Iniciando Class Photo Booth ==="
echo "Usuário atual: $(whoami) (UID: $(id -u), GID: $(id -g))"

# Exportar UID e GID para o docker-compose
export UID=$(id -u)
export GID=$(id -g)

echo "Usando UID=$UID e GID=$GID no container"

# Criar diretórios no host se não existirem
mkdir -p ./flaskapp/photos_originals ./flaskapp/photos_thumbs

echo "Parando containers existentes..."
docker-compose down

echo "Construindo imagem..."
docker-compose build --no-cache

echo "Iniciando aplicação..."
docker-compose up -d

echo "Verificando logs..."
docker-compose logs -f postgres
docker-compose logs -f redis
docker-compose logs -f flaskapp
